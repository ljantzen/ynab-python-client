# SaveTransactionsResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **list[str]** | The transaction ids that were saved | 
**transaction** | [**TransactionDetail**](TransactionDetail.md) | If a single transaction was specified, the transaction that was saved | [optional] 
**transactions** | [**list[TransactionDetail]**](TransactionDetail.md) | If multiple transactions were specified, the transactions that were saved | [optional] 
**duplicate_import_ids** | **list[str]** | If multiple transactions were specified, a list of import_ids that were not were created because of an existing import_id found on the same account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


