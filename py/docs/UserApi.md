# swagger_client.UserApi

All URIs are relative to *https://virtserver.swaggerhub.com/DANIL151002_1/Kursovaya_CREEPER/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_find_phone_get**](UserApi.md#user_find_phone_get) | **GET** /user-find/{phone} | 
[**user_get**](UserApi.md#user_get) | **GET** /user/ | 
[**user_id_delete**](UserApi.md#user_id_delete) | **DELETE** /user/{id} | 
[**user_id_get**](UserApi.md#user_id_get) | **GET** /user/{id} | 
[**user_post**](UserApi.md#user_post) | **POST** /user/ | 

# **user_find_phone_get**
> object user_find_phone_get(phone)



returns a user id by phone number by value or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
phone = 56 # int | Integer

try:
    api_response = api_instance.user_find_phone_get(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_find_phone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **int**| Integer | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> list[object] user_get()



returns all registered users or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()

try:
    api_response = api_instance.user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
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

# **user_id_delete**
> str user_id_delete(id)



Add a new user object or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 56 # int | Integer

try:
    api_response = api_instance.user_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_id_delete: %s\n" % e)
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

# **user_id_get**
> object user_id_get(id)



returns a user by value or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 56 # int | Integer

try:
    api_response = api_instance.user_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_id_get: %s\n" % e)
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

# **user_post**
> str user_post(name, surname, phone, email)



Add a new user object or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
name = 'name_example' # str | Integer
surname = 'surname_example' # str | string
phone = 'phone_example' # str | string
email = 'email_example' # str | string

try:
    api_response = api_instance.user_post(name, surname, phone, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Integer | 
 **surname** | **str**| string | 
 **phone** | **str**| string | 
 **email** | **str**| string | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

