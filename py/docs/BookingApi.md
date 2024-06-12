# swagger_client.BookingApi

All URIs are relative to *https://virtserver.swaggerhub.com/DANIL151002_1/Kursovaya_CREEPER/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**booked_dates_get**](BookingApi.md#booked_dates_get) | **GET** /booked-dates/ | 
[**booking_get**](BookingApi.md#booking_get) | **GET** /booking/ | 
[**booking_id_delete**](BookingApi.md#booking_id_delete) | **DELETE** /booking/{id} | 
[**booking_id_get**](BookingApi.md#booking_id_get) | **GET** /booking/{id} | 
[**booking_post**](BookingApi.md#booking_post) | **POST** /booking/ | 

# **booked_dates_get**
> object booked_dates_get()



returns all booked date times and table ID or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingApi()

try:
    api_response = api_instance.booked_dates_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->booked_dates_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_get**
> list[object] booking_get()



returns all registered bookings or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingApi()

try:
    api_response = api_instance.booking_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->booking_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_id_delete**
> str booking_id_delete(id)



Add a new booking object or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingApi()
id = 56 # int | Integer

try:
    api_response = api_instance.booking_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->booking_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Integer | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_id_get**
> object booking_id_get(id)



returns a booking by value or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingApi()
id = 56 # int | Integer

try:
    api_response = api_instance.booking_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->booking_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Integer | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_post**
> str booking_post(user, table, date_time, guests_count)



Add a new booking object or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BookingApi()
user = 56 # int | user ID integer
table = 56 # int | table ID integer
date_time = 'date_time_example' # str | date and time in string format \"%Y-%m-%d %H:%M:%S\"
guests_count = 56 # int | Integer

try:
    api_response = api_instance.booking_post(user, table, date_time, guests_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingApi->booking_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **int**| user ID integer | 
 **table** | **int**| table ID integer | 
 **date_time** | **str**| date and time in string format \&quot;%Y-%m-%d %H:%M:%S\&quot; | 
 **guests_count** | **int**| Integer | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

