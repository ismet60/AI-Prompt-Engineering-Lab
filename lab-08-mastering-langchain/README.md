# Lab 08 — Mastering LangChain for Advanced Language Model Applications

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Prompt%20Chains-1D9E75?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLM%20API-F55036?style=flat-square)
![Level](https://img.shields.io/badge/Level-Foundational-1D9E75?style=flat-square)

Build a customer-support FAQ and multi-stage prompt workflow using LangChain and Groq, then improve the prompts and evaluate a sample customer query. The model generates text; it does not have access to a real order database.

---

## What You Will Learn

| Skill | Purpose |
| --- | --- |
| Configure Groq | Connect to an available language model without storing a key in code. |
| Build a prompt chain | Extract information and pass results through multiple stages. |
| Improve prompts | Ask for missing information and discourage invented order details. |
| Evaluate responses | Identify unverified claims and compare results across prompt versions. |

## Prerequisites and Dependencies

- Google Colab and a Groq account with an API key and access to the selected model.
- Internet access; Groq usage limits or charges may apply.
- Colab dependencies: `uv`, `langchain`, and `langchain-groq`.
- Local project: Python 3.14 or later and uv; `pyproject.toml` lists `langchain>=1.5.0` and `langchain-groq>=1.1.3`.

## Task 1 — Set Up the Groq API Key

1. Sign in to [Groq Console](https://console.groq.com/) and open **API Keys**.
2. Create a key and keep its value private. Do not include it in code, screenshots, commits, or shared output.
3. In Google Colab, open the **Secrets** panel, add a secret named `GROQ_API_KEY`, paste its value, and enable notebook access.

![Groq sign-in page](<screenshot/2.login _groq.png>)

![Open API keys in Groq](<screenshot/3.0_API_Key.png>)

![Create an API key](<screenshot/3_1_API_Key.png>)

![Choose an API key name](<screenshot/3_2_Create-API_name.png>)

## Install LangChain for Groq with uv

In Colab, run these cells in order:

```python
%pip install -q uv
```

```python
import sys
!uv pip install --python "{sys.executable}" langchain langchain-groq
```

![Install uv and LangChain packages in Colab](<screenshot/04-colab-installation.png>)

![Enable notebook access to the masked Colab secret](<screenshot/05-colab-secret-access.png>)

Load the secret without printing its value:

```python
import os
from google.colab import userdata

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY").strip()
print("Groq API key loaded.")
```

![Load the secret in Colab](<screenshot/06-colab-secret-loaded.png>)

For the local project, run `uv sync` in this folder. A new local project can instead be created with `uv init --no-package`, followed by `uv add langchain langchain-groq`. The original Windows setup is shown below.

![Install project packages locally](<screenshot/1. Langchag-groq.png>)

## Run the Notebook

Open `langchain_lab_public.ipynb` in Colab. Run its setup, secret-loading, Task 2, Task 3, and Task 4 cells in order. The notebook includes the recorded outputs shown below; error outputs have been removed from the sharing copy. If the session restarts, run the setup cells again.

The original lab used a model that was retired. This run uses `openai/gpt-oss-20b` and current LangChain chain syntax; availability depends on the Groq account.

## Task 2 — Customer Support FAQ

The model answers a sample business-hours question. No actual hours were provided; the response is an AI-generated example.

### Code

```python
from langchain_groq import ChatGroq

# Initialize the Groq model.
llm = ChatGroq(
   model="openai/gpt-oss-20b"
)

# Create a simple customer support question.
messages = [
    (
        "system",
        "You are a customer support representative. "
        "Your goal is to efficiently handle queries."
    ),
    ("human", "What are your business hours?"),
]

# Send the messages and display the response.
result = llm.invoke(messages)
print(result.content)
```

### Recorded output

```text
Our customer support team is available Monday through Friday from **9 AM to 6 PM** (local time). If you need assistance outside those hours, feel free to leave a message or submit a ticket, and we’ll get back to you during the next business day.
```

## Task 3 — Multi-stage Prompt Chain

The model extracts the query, responds to a request for order information, and drafts a response. No database is connected; any order details or suggestions are unverified.

### Code

```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Initialize LangChain with the Groq model.
llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

# Step 1: Create the first prompt template to retrieve customer query details.
first_prompt_template = PromptTemplate.from_template(
    "Extract the key information from the following customer query: "
    "{customer_query}"
)

# Step 2: Create the second prompt template to fetch order details
# based on the extracted information.
second_prompt_template = PromptTemplate.from_template(
    "Using the extracted information: {extracted_info}, "
    "retrieve the relevant order details."
)

# Step 3: Create the third prompt template to generate a detailed
# response for the customer.
third_prompt_template = PromptTemplate.from_template(
    "Based on the following order details: {order_details}, "
    "generate a detailed response to address the customer's query."
)

# Step 4: Define the chains using current LangChain syntax.
# StrOutputParser converts each model response into text.
first_chain = first_prompt_template | llm | StrOutputParser()
second_chain = second_prompt_template | llm | StrOutputParser()
third_chain = third_prompt_template | llm | StrOutputParser()

# Input to start the prompt chain: an example customer query.
initial_input = (
    "Can you help me with the status of my order #12345 placed last week?"
)

# Run the first chain to extract key information from the query.
extracted_info = first_chain.invoke({"customer_query": initial_input})
print("Extracted Info:", extracted_info)

# Run the second chain to request order details based on the extracted information.
order_details = second_chain.invoke({"extracted_info": extracted_info})
print("\nOrder Details:", order_details)

# Run the third chain to generate a detailed response based on the order details.
customer_response = third_chain.invoke({"order_details": order_details})
print("\nCustomer Response:", customer_response)
```

### Recorded output

```text
Extracted Info: **Key Information Extracted**

- **Order ID:** 12345  
- **Order Placement Timing:** Last week (exact date not specified)  
- **Requested Action:** Check the current status of the order.

Order Details: I’m sorry, but I don’t have direct access to your order database or the shipping system, so I can’t pull up the live status of order 12345 for you.  

Here’s what you can do next:

| Option | How to do it | What to look for |
|--------|--------------|------------------|
| **Check the order confirmation email** | Open the email you received when you placed the order. | Look for a tracking number or a link that says “View Order Status.” |
| **Log in to the retailer’s website** | Go to the site’s “My Orders” or “Order History” section. | Find order 12345 and see the current status (e.g., “Processing,” “Shipped,” “Out for delivery,” etc.). |
| **Use the mobile app** | If the retailer has an app, open it and navigate to your orders. | Same as above – you’ll see the status and any tracking info. |
| **Contact Customer Support** | Call the support line, use live chat, or send an email. | Provide the order ID (12345) and ask for the current status and expected delivery date. |
| **Track the shipment** | If you have a tracking number, enter it on the carrier’s website (UPS, FedEx, DHL, USPS, etc.). | You’ll see the most recent location and estimated delivery. |

If you let me know which retailer or carrier you’re dealing with, I can give you the exact URL or phone number to use. Otherwise, any of the steps above should get you the information you need.

Customer Response: **Subject: Quick Guide to Check the Status of Order 12345**

Hi there,

I’m sorry I don’t have direct access to your order database, so I can’t pull up the live status of order 12345 right now. However, there are a few reliable ways you can find the most up‑to‑date information on your shipment. Below is a detailed, step‑by‑step guide that covers every option.

| **Option** | **How to do it** | **What to look for** |
|------------|------------------|----------------------|
| **1. Check the order confirmation email** | • Open the email you received when you placed the order.<br>• Search for “Order 12345” or the order number in the subject line or body.<br>• Look for a “Track Order” link or a tracking number (often a series of letters and numbers). | • Tracking number (e.g., 1Z999AA10123456784).<br>• A link that says “View Order Status” or “Track Shipment.” |
| **2. Log in to the retailer’s website** | • Visit the retailer’s homepage.<br>• Sign in to your account.<br>• Go to **My Orders** / **Order History**.<br>• Locate order 12345. | • Current status (e.g., “Processing,” “Shipped,” “Out for delivery”).<br>• Any available tracking number or link. |
| **3. Use the retailer’s mobile app** | • Open the app (if you have it installed).<br>• Tap **Orders** or **My Orders**.<br>• Find order 12345. | Same as above—status and tracking info. |
| **4. Track the shipment directly** | • If you have a tracking number, copy it.<br>• Visit the carrier’s website (UPS, FedEx, DHL, USPS, etc.).<br>• Paste the number into the tracking field and hit **Track**. | • Real‑time location, last scan, estimated delivery date. |
| **5. Contact Customer Support** | • Call the retailer’s support line.<br>• Use live chat on the website or app.<br>• Send an email to the support address. | • Provide order ID (12345).<br>• Ask for the current status and expected delivery date. |

### Need a Specific Link or Phone Number?
If you let me know which retailer or carrier you’re dealing with, I can give you the exact URL or phone number to use. For example:

- **Amazon**:  
  - Website: https://www.amazon.com/your-account/orders  
  - Phone: 1‑888‑280‑4331 (U.S.)  
- **eBay**:  
  - Website: https://www.ebay.com/mysite?tab=orders  
  - Phone: 1‑888‑308‑9100 (U.S.)  
- **UPS**:  
  - Tracking: https://www.ups.com/track?loc=en_US  
  - Phone: 1‑800‑742‑5877 (U.S.)  
- **FedEx**:  
  - Tracking: https://www.fedex.com/apps/fedextrack/  
  - Phone: 1‑800‑463‑3339 (U.S.)  

If you’re not sure which retailer or carrier it is, just let me know the name of the store or the brand you purchased from, and I’ll fetch the appropriate contact details for you.

---

#### Quick Tips

- **If you can’t find the confirmation email**: Search your inbox (and spam/junk folders) for the retailer’s name or for “order confirmation.”  
- **If the order is still “Processing”**: Shipping usually begins within 1–3 business days.  
- **If the order is “Shipped” but the tracking says “In transit”**: It may be a few days before it arrives.  
- **If the tracking shows “Delivered” but you haven’t received it**: Check with neighbors or the front desk, and then contact the carrier’s customer service.  

Let me know if you’d like me to look up the specific link or phone number for your retailer/carrier, or if there’s anything else I can help with. Happy to help you get that package where it belongs!
```

## Task 4 — Improve and Evaluate Prompts

The prompts ask the model to identify missing information and avoid invented details. This recorded run uses one query; test another query separately to complete the lab’s comparison of different queries. The model’s suggested identity checks are not verified company policy.

### Code

```python
# Improved Prompt 1
first_prompt_template = PromptTemplate.from_template(
    "Extract the order number and customer request from: {customer_query}. "
    "If a detail is missing, say 'not provided'."
)

# Improved Prompt 2
second_prompt_template = PromptTemplate.from_template(
    "Using only the information in {extracted_info}, list the "
    "information needed to check the order status. Do not give "
    "example names, addresses, dates, payment details, or order statuses."
)

# Improved Prompt 3
third_prompt_template = PromptTemplate.from_template(
    "Using only {order_details}, write a short customer response. "
    "Do not address the customer by name or include example personal "
    "information. State that the actual order status must be verified."
)
# Create the chains using the improved prompts.
first_chain = first_prompt_template | llm | StrOutputParser()
second_chain = second_prompt_template | llm | StrOutputParser()
third_chain = third_prompt_template | llm | StrOutputParser()

# Test with a customer query.
initial_input = "Can you help me with the status of my order #12345 placed last week?"

# Run the first chain.
extracted_info = first_chain.invoke({"customer_query": initial_input})
print("Extracted Info:", extracted_info)

# Run the second chain.
order_details = second_chain.invoke({"extracted_info": extracted_info})
print("\nOrder Details Needed:", order_details)

# Run the third chain.
customer_response = third_chain.invoke({"order_details": order_details})
print("\nCustomer Response:", customer_response)
```

### Recorded output

```text
Extracted Info: Order number: **12345**  
Customer request: **status of my order**

Order Details Needed: **Information required to check an order status**

- Order number  
- Customer email address (or account ID)  
- Phone number used during checkout  
- Shipping address (street, city, state/province, postal code)  
- Billing address (if different from shipping)  
- Payment method identifier (e.g., last four digits of card, PayPal ID)  

These are the typical pieces of data that a support agent would request in order to locate and verify the status of an order.

Customer Response: To locate and verify your order, please provide the following details:

- Order number  
- Customer email address or account ID  
- Phone number used at checkout  
- Shipping address (street, city, state/province, postal code)  
- Billing address (if different from shipping)  
- Payment method identifier (e.g., last four digits of card, PayPal ID)

Once we have this information, we can verify the actual order status.
```

## Key Takeaway

Prompt instructions influence the response but cannot guarantee correctness. A real customer-support system must use an authorized data source and approved identity-verification procedures. Review any model-generated business hours, customer details, and order information before use.

## Project Files

| File | Purpose |
| --- | --- |
| `langchain_lab_public.ipynb` | Notebook code and recorded results; error outputs removed for sharing. |
| `faq_example.py` | Local FAQ example; after setting the key privately, run `uv run python faq_example.py`. |
| `pyproject.toml` and `uv.lock` | Python requirements and dependency lockfile. |
| `screenshot/` | Selected Groq, local setup, and Colab setup screenshots. |

[← Back to all labs](../README.md)
