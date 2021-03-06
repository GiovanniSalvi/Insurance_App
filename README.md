# Insurance_App

### Here are the business rules.

Insurance is only sold if required by the customer.

If the package is being sent to the UK, insurance charge is 1% of the value of the item.

If the package is being sent to France, Germany, the Netherlands or Belgium, insurance charge is 1.5% of the value of the item.

If the package is being sent anywhere else in the world, insurance charge is 4% of the value of the item.

If the package is worth more than £10,000, we cannot insure it and these orders must not be accepted by the system.

The insurance charge is rounded to the nearest £0.01

If the insurance charge is calculated to be less than £9, then it's rounded up to £9 (£9 is the minimum charge)

The insurance charge already includes Insurance Premium Tax (IPT) at 12%, i.e. insurance_charge_without_tax * 1.12 = insurance_charge

Orders can only be accepted once. If the same tracking number is used again, the 2nd order should be rejected.

Do not accept orders where the despatch date is not today or tomorrow.

Orders are PUT to /orders

Accepted orders can be retrieved by a GET to /orders/<order_id>

### Example Request
{
  "sender": {
    "name": "Carole's Computers",
    "street_address": "123 Castle Street",
    "city": "Birmingham",
    "country_code": "GB"
  },
  "recipient": {
    "name": "Angela Schmidt",
    "street_address": "123 Schloßstraße",
    "city": "Berlin",
    "country_code": "DE"
  },
  "value": "1234.50",
  "despatch_date": "2021-09-01",
  "contents declaration": "Laptop",
  "insurance_required": true,
  "tracking_reference": "GBDE1231239090"
}
Example response to the example request
{
  "package": {
    "sender": {
      "name": "Carole's Computers",
      "street_address": "123 Castle Street",
      "city": "Birmingham",
      "country_code": "GB"
    },
    "recipient": {
      "name": "Angela Schmidt",
      "street_address": "123 Schloßstraße",
      "city": "Berlin",
      "country_code": "DE"
    },
    "value": "1234.50",
    "despatch_date": "2021-09-01",
    "contents declaration": "Laptop",
    "insurance_required": true,
    "tracking_reference": "GBDE1231239090"
  },
  "order_url": "http://localhost:8080/order/1",
  "accepted_at": "2021-09-01T12:22:43.406768",
  "insurance_provided": true,
  "total_insurance_charge": "18.52",
  "ipt_included_in_charge": "1.98"
}
The data from the request is echoed back in the response in the "package" field, the rest of the response is generated by the app.
