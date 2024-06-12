# swagger_client.TableApi

All URIs are relative to *https://virtserver.swaggerhub.com/DANIL151002_1/Kursovaya_CREEPER/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**table_get**](TableApi.md#table_get) | **GET** /table/ | 
[**table_id_delete**](TableApi.md#table_id_delete) | **DELETE** /table/{id} | 
[**table_id_get**](TableApi.md#table_id_get) | **GET** /table/{id} | 
[**table_post**](TableApi.md#table_post) | **POST** /table/ | 

# **table_get**
> list[object] table_get()



returns all registered tables or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TableApi()

try:
    api_response = api_instance.table_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->table_get: %s\n" % e)
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

# **table_id_delete**
> str table_id_delete(id)



Add a new Table object or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TableApi()
id = 56 # int | Integer

try:
    api_response = api_instance.table_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->table_id_delete: %s\n" % e)
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

# **table_id_get**
> object table_id_get(id)



returns a table by value or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TableApi()
id = 56 # int | Integer

try:
    api_response = api_instance.table_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->table_id_get: %s\n" % e)
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

# **table_post**
> object table_post()



Add a new Table object or string \"Failed\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TableApi()

try:
    api_response = api_instance.table_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableApi->table_post: %s\n" % e)
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

