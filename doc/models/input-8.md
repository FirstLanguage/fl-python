
# Input 8

## Structure

`Input8`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lang` | `string` | Required | Allowed language code. Refer Allowed languages section. |
| `content_type` | `string` | Required | Allowed values or html or text. If html is specified all html tags and special characters will be stripped before processing. |
| `url` | `string` | Required | URL where the text for the NER task is stored. |

## Example (as JSON)

```json
{
  "lang": "lang2",
  "contentType": "contentType6",
  "url": "url4"
}
```
