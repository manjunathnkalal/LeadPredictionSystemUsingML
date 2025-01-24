from django.db import models
from django.core.validators import MinValueValidator

class Inputmodel(models.Model):
    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    LEAD_ORIGIN_CHOICES = [
        ("API","API"),
        ("Landing Page Submission","Landing Page Submission"),
        ("Lead Add Form","Lead Add Form"),
        ("Lead Import","Lead Import"),
    ]

    LEAD_SOURCE_CHOICES = [
        ("bing","bing"),
        ("blog","blog"),
        ("Click2call","Click2call"),
        ("Direct Traffic","Direct Traffic"),
        ("google","google"),
        ("Google","Google"),
        ("Facebook","Facebook"),
        ("Live Chat","Live Chat"),
        ("NC_EDM","NC_EDM"),
        ("Olark Chat","Olark Chat"),
        ("Organic Search","Organic Search"),
        ("Pay per Click Ads","Pay per Click Ads"),
        ("Press_Release","Press_Release"),
        ("Reference","Reference"),
        ("Referral Sites","Referral Sites"),
        ("Social Media","Social Media"),
        ("testone","testone"),
        ("WeLearn","WeLearn"),
        ("welearnblog_Home","welearnblog_Home"),
        ("Welingak Website","Welingak Website"),
        ("youtubechannel","youtubechannel"),
    ]
    
    LAST_ACTIVITY_CHOICES = [
            ("Approached upfront","Approached upfront"),
            ("Converted to Lead","Converted to Lead"),
            ("Email Bounced","Email Bounced"),
            ("Email Link Clicked","Email Link Clicked"),
            ("Email Marked Spam","Email Marked Spam"),
            ("Email Opened","Email Opened"),
            ("Email Received","Email Received"),
            ("Form Submitted on Website","Form Submitted on Website"),
            ("Had a Phone Conversation","Had a Phone Conversation"),
            ("Olark Chat Conversation","Olark Chat Conversation"),
            ("Page Visited on Website","Page Visited on Website"),
            ("Resubscribed to emails","Resubscribed to emails"),
            ("SMS Sent","SMS Sent"),
            ("Unreachable","Unreachable"),
            ("Unsubscribed","Unsubscribed"),
            ("View in browser link Clicked","View in browser link Clicked"),
            ("Visited Booth in Tradeshow","Visited Booth in Tradeshow"),
]
    
    SPECIALIZATIONS_CHOICES = [
            ("Banking, Investment And Insurance","Banking, Investment And Insurance"),
            ("Business Administration","Business Administration"),
            ("E-Business","E-Business"),
            ("E-COMMERCE","E-COMMERCE"),
            ("Finance Management","Finance Management"),
            ("Healthcare Management","Healthcare Management"),
            ("Hospitality Management","Hospitality Management"),
            ("Human Resource Management","Human Resource Management"),
            ("International Business","International Business"),
            ("IT Projects Management","IT Projects Management"),
            ("Marketing Management","Marketing Management"),
            ("Media and Advertising","Media and Advertising"),
            ("Operations Management","Operations Management"),
            ("Others","Others"),
            ("Retail Management","Retail Management"),
            ("Rural and Agribusiness","Rural and Agribusiness"),
            ("Services Excellence","Services Excellence"),
            ("Supply Chain Management","Supply Chain Management"),
            ("Travel and Tourism","Travel and Tourism"),
    ]

    CURRENT_OCCUPATION_CHOICES = [
        ("Businessman","Businessman"),
        ("Housewife","Housewife"),
        ("Other","Other"),
        ("Student","Student"),
        ("Unemployed","Unemployed"),
        ("Working Professional","Working Professional"),
    ]

    TAGS_CHOICES = [
        ("Already a student","Already a student"),
        ("Busy","Busy"),
        ("Closed by Horizzon","Closed by Horizzon"),
        ("Interested  in full time MBA","Interested  in full time MBA"),
        ("Interested in other courses","Interested in other courses"),
        ("Lost to EINS","Lost to EINS"),
        ("No comments","No comments"),
        ("Not doing further education","Not doing further education"),
        ("OTHER_COMMENT","OTHER_COMMENT"),
        ("Ringing","Ringing"),
        ("switched off","switched off"),
        ("Will revert after reading the email","Will revert after reading the email"),
    ]

    LEAD_QUALITY_CHOICES = [
        ("High in Relevance","High in Relevance"),
        ("Low in Relevance","Low in Relevance"),
        ("Might be","Might be"),
        ("Not Sure","Not Sure"),
        ("Worst","Worst"),
    ]

    CITY_CHOICES = [
        ("Mumbai","Mumbai"),
        ("Other Cities","Other Cities"),
        ("Other Cities of Maharashtra","Other Cities of Maharashtra"),
        ("Other Metro Cities","Other Metro Cities"),
        ("Thane & Outskirts","Thane & Outskirts"),
        ("Tier II Cities","Tier II Cities"),
    ]

    LAST_NOTABLE_ACTIVITY_CHOICES = [
        ("Approached upfront","Approached upfront"),
        ("Email Bounced","Email Bounced"),
        ("Email Link Clicked","Email Link Clicked"),
        ("Email Marked Spam","Email Marked Spam"),
        ("Email Opened","Email Opened"),
        ("Email Received","Email Received"),
        ("Form Submitted on Website","Form Submitted on Website"),
        ("Had a Phone Conversation","Had a Phone Conversation"),
        ("Modified","Modified"),
        ("Olark Chat Conversation","Olark Chat Conversation"),
        ("Page Visited on Website","Page Visited on Website"),
        ("Resubscribed to emails","Resubscribed to emails"),
        ("SMS Sent","SMS Sent"),
        ("Unreachable","Unreachable"),
        ("Unsubscribed","Unsubscribed"),
        ("View in browser link Clicked","View in browser link Clicked"),
    ]

    total_visits = models.IntegerField(validators=[MinValueValidator(1)])
    total_time_spent_on_website = models.IntegerField(validators=[MinValueValidator(1)])
    page_views_per_visit = models.IntegerField(validators=[MinValueValidator(1)])
    lead_origin = models.CharField(max_length=255, choices=LEAD_ORIGIN_CHOICES)
    lead_source = models.CharField(max_length=255, choices=LEAD_SOURCE_CHOICES)
    last_activity = models.CharField(max_length=255, choices=LAST_ACTIVITY_CHOICES)
    specialization = models.CharField(max_length=255, choices=SPECIALIZATIONS_CHOICES)
    current_occupation = models.CharField(max_length=255, choices=CURRENT_OCCUPATION_CHOICES)
    tags = models.CharField(max_length=255, choices=TAGS_CHOICES)
    lead_quality = models.CharField(max_length=255, choices=LEAD_QUALITY_CHOICES)
    city = models.CharField(max_length=255, choices=CITY_CHOICES)
    do_not_email = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    last_notable_activity = models.CharField(max_length=255, choices=LAST_NOTABLE_ACTIVITY_CHOICES)
    free_copy_of_mastering_the_interview = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    status = models.CharField(max_length=50, blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    case = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return (f"Inputs: ({self.total_visits}, {self.total_time_spent_on_website}, {self.page_views_per_visit}, "
                f"{self.lead_origin}, {self.lead_source}, {self.last_activity}, {self.specialization}, "
                f"{self.current_occupation}, {self.tags}, {self.lead_quality}, {self.city}, {self.do_not_email}, "
                f"{self.last_notable_activity}, {self.free_copy_of_mastering_the_interview}), "
                f"Status: {self.status}, Probability: {self.probability}, Case: {self.case}")
