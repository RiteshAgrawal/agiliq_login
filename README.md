agiliq_login
============

I have used Django for the given task.
first I have registerd on join.agiliq.com and access client_id and client secret.
Here I first send a get request with required parameters to authorisation url and redirect it back to my localhost.
In this I will get code along with the state that I mentioned earlier in the authorisation url.

Now In the second pass if I if state is same then send POST request for access tken. I have used requests module for this task. After getting the access token i created a form and submit the required data as multipart-form because of pdf file.


