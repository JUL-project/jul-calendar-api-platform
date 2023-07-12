from typing import Union
import datetime

class calenderServer:
    
    # init object for OAuth2.0 and Status in permission
    def __init__(self: object,
                 OAuth: callable, 
                 permissions: int = 0):
        self.status = 'https://www.googleapis.com/auth/calendar'
        self.OAuth = OAuth
        if permissions == 0:
            self.status = self.status + ".readonly"

    # Get google token and access
    def getGoogle(self: object, 
                  port: int = 0):
        
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        
        flow = InstalledAppFlow.from_client_secrets_file(self.OAuth, self.status)
        creds = flow.run_local_server(port)
        self.service = build('calendar', 'v3', credentials=creds)
        
        
        # data = dict(\
        #     code=authCode,\
        #     client_id=self.GOOGLE_API_CLIENT_ID,\
        #     client_secret=self.GOOGLE_API_CLIENT_SECRET,\
        #     grant_type="authorization_code",\
        #     redirect_uri=self.GOOGLE_API_REDIRECT_URL
        # )

        # response, content = http.request(url, "POST",
        #     headers=headers,
        #     body=urlencode(data)
        # )

        # jc = json.loads(content)
        # print(content)
        # return jc['refresh_token']
    
    # Get info GoogleCalendar
    def checkGoogle(self: object,
                    calendar_id: str = 'primary',
                    startDate: str = None,
                    endDate: str = None,
                    max_results: int = 250,
                    is_single_events: bool = True,
                    orderby: str = 'startTime'
                    ):
            
        today = datetime.date.today().isoformat()
        if startDate is None:
            time_min = today + 'T00:00:00+09:00'
        if endDate is None : 
            time_max = today + 'T23:59:59+09:00'
            
        # 바로 조회할 시
        if not self.service:
            self.getGoogle()
        
        events_result = self.service.events().list(calendarId = calendar_id,
                                            timeMin = time_min,
                                            timeMax = time_max,
                                            maxResults = max_results,
                                            singleEvents = is_single_events,
                                            orderBy = orderby
                                            ).execute()

        
        return events_result['items']
        
# Need to fix with Flask or Module
if __name__ == '__main__' :
    
    calenders = calenderServer()
    
    
    
    
    
    
    
    
    
    
    
    

    