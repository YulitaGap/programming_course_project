
import http.client

conn = http.client.HTTPSConnection("api.dexcom.com")

payload = "{  \n   \"targetRanges\":[  \n      {  \n         \"name\":\"day\",\n         \"startTime\":\"06:00:00\",\n         \"endTime\":\"22:00:00\",\n         \"egvRanges\":[\n           {\n            \"name\": \"urgentLow\",\n            \"bound\": 55\n          },\n          {\n            \"name\": \"low\",\n            \"bound\": 70\n          },\n          {\n            \"name\": \"high\",\n            \"bound\": 180\n          }\n         ]\n      },\n      {  \n         \"name\":\"night\",\n         \"startTime\":\"22:00:00\",\n         \"endTime\":\"06:00:00\",\n         \"egvRanges\":[\n           {\n            \"name\": \"urgentLow\",\n            \"bound\": 55\n          },\n           {\n            \"name\": \"low\",\n            \"bound\": 80\n          },\n          {\n            \"name\": \"high\",\n            \"bound\": 200\n          }\n         ]\n      }\n   ]\n}"

headers = {
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IncyYUVpQmRlMXBfNnNjZmMzXzFpeHFvaDVqTSIsImtpZCI6IncyYUVpQmRlMXBfNnNjZmMzXzFpeHFvaDVqTSJ9.eyJpc3MiOiJodHRwczovL3VhbTEuZGV4Y29tLmNvbS9pZGVudGl0eSIsImF1ZCI6Imh0dHBzOi8vdWFtMS5kZXhjb20uY29tL2lkZW50aXR5L3Jlc291cmNlcyIsImV4cCI6MTU1MDc4OTMxOCwibmJmIjoxNTUwNzgyMTE4LCJjbGllbnRfaWQiOiJhMG10bmJQc0tvd1hqNHFSQzNYUmhvRXBDSnJXelh0TyIsInNjb3BlIjpbIm9mZmxpbmVfYWNjZXNzIiwiZWd2IiwiY2FsaWJyYXRpb24iLCJkZXZpY2UiLCJzdGF0aXN0aWNzIiwiZXZlbnQiXSwic3ViIjoiYjJkOTNiYTItOWQ4OS00ZWU4LTkyYTEtMzllYzIzMzU5MmZhIiwiYXV0aF90aW1lIjoxNTUwNzY4OTk3LCJpZHAiOiJpZHNydiIsImp0aSI6ImRmOGEzNjJhZTgyMzU3Mzk3NDljOTBiY2RkYjRmYWYzIiwiYW1yIjpbInBhc3N3b3JkIl19.KjyIyPwhYcf_eWoRZkJlK_XmFOX1K8OTJz0nIqwiwVrvZ4E9wI89TANgCErPSjLuGXTIaiQkUPQWuwsLiDJpSsP_mnU4o4RX-m1dgwzMZX6uhyqCIVhoG5XRuu8UugPjkQ_IybB5Spvdvrmd18_ScZdnvv9rdgtBoMriy0QzmvyttCTGEVAWkQlBMApGWE8WCZ9tYUWtzuxanSgjZCf3huylT_OBn29jAr5LwPV19oNMZtrFUyq15wcJ3KTPlenvoZahtiRqXPucE4etbJyWYSemrbmkEHCwLY1i9WWGZSPie353-7EQ8w3lcvnI1NBz0hbKRLLiTp7NaV5TgfuDeQ",
    'content-type': "application/json"
    }

conn.request("POST", "/v2/users/self/statistics?startDate=2017-06-01&endDate=2017-06-17", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))