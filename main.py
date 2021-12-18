import http.client
import json

class Test_WebApi:
   
    def upload(self):
        self.link1 = http.client.HTTPSConnection("content.dropboxapi.com")
        payload = ''
        headers = {
            'Dropbox-API-Arg': '{"path": "/New_file.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
            'Content-Type': 'application/octet-stream',
            'Authorization': 'Bearer b7K1oKEX1XoAAAAAAAAAAZa5fUeVPvfZwovy0oaiPeg7sSEWauYI24yUfpS2BcTG'
        }
        self.link1.request("POST", "/2/files/upload", payload, headers)
        assert self.link1.getresponse().status == 200, "test with upload failed"

    def get_file_metadata(self):
        self.link2 = http.client.HTTPSConnection("api.dropboxapi.com")
        payload = json.dumps({
            "path": "/New_file.txt",
            "include_media_info": False,
            "include_deleted": False,
            "include_has_explicit_shared_members": False
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer b7K1oKEX1XoAAAAAAAAAAZa5fUeVPvfZwovy0oaiPeg7sSEWauYI24yUfpS2BcTG'
        }
        self.link2.request("POST", "/2/files/get_metadata", payload, headers)
        assert self.link2.getresponse().status == 200, "test with file metadata failed"

    def delete_file(self):
        self.link3 = http.client.HTTPSConnection("api.dropboxapi.com")
        payload = json.dumps({
            "path": "/New_file.txt"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer b7K1oKEX1XoAAAAAAAAAAZa5fUeVPvfZwovy0oaiPeg7sSEWauYI24yUfpS2BcTG'
        }
        self.link3.request("POST", "/2/files/delete_v2", payload, headers)
        assert self.link3.getresponse().status == 200, "test with  failed"

test = Test_WebApi()
test.upload()
test.get_file_metadata()
test.delete_file()
