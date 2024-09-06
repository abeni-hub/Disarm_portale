from django.db import models

# Define choices as tuples for each attribute
STRATEGY_CHOICES = [
    ('Determine Target Audience','Determine Target Audience'),
    ('Determine Target Ends','Determine Target Ends'),
]

OBJECTIVE_CHOICES = [
    ('Facilitate State Propaganda', 'Facilitate State Propaganda'),
    ('Degrade Adversary', 'Degrade Adversary'),
    ('Dismiss', 'Dismiss'),
    ('Discredit Credible Sources', 'Discredit Credible Sources'),
    ('Distort', 'Distort'),
    ('Distract', 'Distract'),
    ('Dismay', 'Dismay'),
    ('Divide', 'Divide'),
]

TARGET_AUDIENCE_CHOICES = [
    ('Segement Audience', 'Segement Audience'),
    ('Geographic Segmentation', 'Geographic Segmentation'),
    ('Demographic', 'Demographic Segmentation'),
    ('Economic', 'Economic Segmentation'),
    ('psychographic', 'Psychographic Segmentation'),
    ('political', 'Political Segmentation'),
    ('Map Target', 'Map Target Audience Information Environment'),
    ('Monitor Social Media Analytics', 'Monitor Social Media Analytics'),
    ('Evaluate', 'Evaluate Media Surveys'),
    ('Identify Trending Topics/Hashtags', 'Identify Trending Topics/Hashtags'),
    ('Conduct web', 'Conduct Web Trending Analysis'),
    ('Assess Degree', 'Access Degree/Type of Media Access'),
    ('Identify social', 'Identify social and Technical Vulnerabilities'),
    ('Find Echo Chambers', 'Find Echo Chambers'),
    ('Identify', 'Identify Data Voids'),
    ('Identify Existing Prejudices', 'Identify Existing Prejudices'),
    ('Identify Existing Fissures', 'Identify Existing Fissures'),
    ('Identify Existing Conspiracy', 'Identify Existing Conspiracy Narrative/Suspicions'),
    ('Identify Wedge Issues', 'Identify Wedge Issues'),
    ('Identify Target Audience Adversaries', 'Identify Target Audience Adversaries'),
    ('Identify Media System Vulnerabilities', 'Identify Media System Vulnerabilities'),

]

# Define Plan model
class Plan(models.Model):
    strategy = models.CharField(max_length=300, choices=STRATEGY_CHOICES)
    objective = models.CharField(max_length=300, choices=OBJECTIVE_CHOICES)
    target_audience_analysis = models.CharField(max_length=300, choices=TARGET_AUDIENCE_CHOICES)
    additional_details = models.JSONField(blank=True, null=True, help_text="Additional details based on selected choices")

    def __str__(self):
        return f"{self.strategy} - {self.objective} - {self.target_audience_analysis}"
# Prepare model with its choices
NARRATIVE_CHOICES = [

    ('Leverage Existing Narratives', 'Leverage Existing Narratives'),
    ('Develop Competing Narratives', 'Develop Competing Narratives'),
    ('Leverage Conspiracy Theory Narrative', 'Leverage Conspiracy Theory Narrative'),
    ('Amplify Existing Conspiracy Theory Narrative', 'Amplify Existing Conpiracy Theory Narrative'),
    ('Develop Original Conspiracy Theory Narrative', 'Develop Original Conspiracy Theory Narrative'),
    ('Demand insurmountable proof', 'Demand insurmountable proof'),
    ('Respond to','Respond to Breaking News Event'),
    ('Develop New Narratives','Develp New Narratives'),
    ('Integrate Target Audience Vulnerabilities', 'Integrate Target Audience Vulnerabilities into Narrative'),

]

CONTENT_CHOICES = [
    ('Craft hashtags and search artifacts', 'Craft hashtags and search artifacts'),
    ('Generate information pollution', 'Generate information pollution'),
    ('Create fake research', 'Create fake research'),
    ('Hijack Hashtags', 'Hijack Hashtags'),
    ('Distort facts', 'Distort facts'),
    ('Reframe Context', 'Edit Open-Source Content'),
    ('Edit Open-Source content', 'Edit Open-Source content'),
    ('Reuse Existing content', 'Reuse Existing content'),
    ('Use CopyPaste', 'Use Copypaste'),
    ('Plagiarize Content', 'Plagiarize Content'),
    ('Deceptive Labeled or Translated', 'Deceptive Labeled or Translated'),
    ('Appropriate Content', 'Appropriate Content'),
    ('Develop Text-Based Content', 'Develop Text-Based Content'),
    ('Develop AI generated Text', 'Develop AI generated Text'),
    ('Develop False or Altered Documents', 'Develop False or Altered Documents'),
    ('Develop inauthentic News Articles', 'Develop inauthentic News Articles'),
    ('Develop image-based Content', 'Develop image-based Content'),
    ('Develop Memes', 'Develop Memes'),
    ('Develop AI Generated Images(Deepfakes)', 'Develop AI Generated Images(Deepfakes)'),
    ('Deceptively Edit Images(Cheap fakes)', 'Deceptively Edit Images(Cheap fakes)'),
    ('Aggregate information into Evidence Collages', 'Aggregate information into Evidence Collages'),
    ('Develop vidio-based Content', 'Develop vidio-based Content'),
    ('Deceptively Edit Vidio(Cheap fakes)', 'Deceptively Edit Vidio(Cheap fakes)'),
    ('Develop Audio-Based Content', 'Develop Audio-Based Content'),
    ('Develop AI-Generated Audio(cheap fake)', 'Develop AI-Generated Audio(cheap fake)'),
    ('Deceptively Edit Audio(cheap fake)', 'Deceptively Edit Audio(cheap fake)'),
    ('Obtain Authentic Documents', 'Obtain Authentic Documents'),
    ('Create inauthentic Documents', 'Create inauthentic Documents'),
    ('Alter inauthentic Documents', 'Alter inauthentic Documents'),

]
SOCIAL_ASSETS_CHOICES = [
    ('create', 'create inauthentic social media pages'),
    ('Cultivate', 'Cultivate ignorant agents'),
    ('create inauthentic websites', 'create inauthentic websites'),
    ('Prepare', 'prepare fundraising campaigns'),
    ('Raise funds', 'Raise funds from malign actors'),
    ('Raise funds', 'Raise funds from ignorant agents'),
    ('Prepare Physical Broadcast Capablities', 'Prepare Physical Broadcast Capablities'),
    ('Create inauthentic Accounts', 'Create inauthentic Accounts'),
    ('Create Anonymous Accounts', 'Create Anonymous Accounts'),
    ('Create Cyborg Accounts', 'Create Cyborg Accounts'),
    ('Create Bot Accounts', 'Create Bot Accounts'),
    ('Create Sockpuppet Accounts', 'Create Sockpuppet Accounts'),
    ('Recruit malign actors', 'Recruit malign actors'),
    ('Recruit contractors', 'Recruit contractors'),
    ('Recruit Partisans', 'Recruit Partisians'),
    ('Recruit contractors', 'Recruit contractors'),
    ('Enlist Troll Accounts', 'Enlist Troll Accounts'),
    ('Build Network', 'Build Network'),
    ('Create Organizations', 'Create Organizations'),
    ('Use Follow Trains', 'Use Follow Trains'),
    ('Create Community or sub-group', 'Create Community or sub-group'),
    ('Acquire/Recruit', 'Acquire/Recruit'),
    ('Fund Proxies', 'Fund Proxies'),
    ('Acquire Botnets', 'Acquire Botnets'),
    ('Infiltrate Existing Networks', 'Infiltrate Existing Networks'),
    ('Identify susceptible targets in networks', 'Identify susceptible targets in networks'),
    ('Utilize Butterfly Attacks', 'Utilize Butterfly Attacks'),
    ('Develop Owned Media Assets', 'Develop Owned Media Assets'),
    ('Leverage Content Farms', 'Leverage Content Farms'),
    ('Create Content Farms', 'Create Content Farms'),
    ('Outsource Content Creation to External Organizations', 'Outsource Content Creation to External Organizations'),

]
LEGITIMACY_CHOICES = [
    ('create fake experts', 'create fake experts'),
    ('utilize', 'Utilize Academic'),
    ('compromise legitimate accounts', 'Compromise legitimate accounts'),
    ('create personas', 'create personas'),
    ('Backstop personas', 'Backstop personas'),
    ('Create inauthentic News Sites', 'Create inauthentic News Sites'),
    ('Leverage Existing Inauthentic News Site', 'Leverage Existing Inauthentic News Site'),
    ('prepare Assets impersonating Legitimate entities', 'prepare Assets impersonating Legitimate entities'),
    ('Astroturfing', 'Astroturfing'),
    ('Spoof/parody account/site', 'Spoof/parody account/site'),
    ('Co-Opt Trusted Sources','Co-Opt Trusted Sources'),
    ('Co-Opt Trusted Individuals','Co-Opt Trusted Individuals'),
    ('Co-Opt Grassroots Groups','Co-Opt Grassroots Groups'),
    ('Co-Opt Influencers','Co-Opt Influencers'),

]

MICROTARGET_CHOICES = [
    ('create click', 'Create Clickbait'),
    ('Purchase Targeted Advertisements', 'Purchase Targeted Advertisements'),
    ('Create localized Content', 'Create localized Content'),
    ('Leverage Echo Chambers/Filter Bubbles', 'Leverage Echo Chambers/Filter Bubbles'),
    ('Use existing Echo Chambers', 'Use existing Echo Chambers/Filter Bubbles'),
    ('Create Echo Chambers', 'Create Echo Chambers/Filter Bubbles'),
    ('Exploit Data Voids', 'Exploit Data Voids'),


]

CHANNEL_CHOICES = [
    ('Online Polls', 'Online Polls'),
    ('Chat apps.', 'Chat apps'),
    ('Use Encrypted Chat apps', 'Use Encrypted Chat apps'),
    ('Use UnEncrypted Chat apps', 'Use UnEncrypted Chat apps'),
    ('Livestream', 'Livestream'),
    ('Video Livestream', 'Video Livestream'),
    ('Audio Livestream', 'Audio Livestream'),
    ('Social Networks', 'Social Networks'),
    ('Mainstream Social Networks', 'Mainstream Social Networks'),
    ('Dating App', 'Dating App'),
    (' Social Networks', 'private/Closed Social Networks'),
    (' Interest Networks', 'Interest Based Networks'),
    (' use Hashtags', 'use Hashtag'),
    ('Create dedicated hashtag', 'Create dedicated hashtag'),
    ('Media Sharing Networks', 'Media Sharing Networks'),
    ('Photo Sharing', 'Photo Sharing'),
    ('Vidio Sharing', 'Vidio Sharing'),
    ('Audio Sharing', 'Audio Sharing'),
    ('Discussion Form', 'Discussion Form'),
    ('Anonymous Message boards', 'Anonymous Message boards'),
    ('Bookmarking and Content','Bookmarking and content Curation'),
    ('Blogging','Blogging and Publishing Networks'),
    ('Consumer Review Networks', 'Consumer Review Networks'),
    ('Formal Diplomatic Channels','Formal Diplomatic Channels'),
    ('Traditional Media','Traditional Media'),
    ('TV','TV'),
    ('Newspaper','Newspaper'),
    ('Radio','Radio'),
    ('Email','Email'),

]



class Prepare(models.Model):
    narrative = models.CharField(max_length=500, choices=NARRATIVE_CHOICES)
    content = models.CharField(max_length=500, choices=CONTENT_CHOICES)
    social_assets = models.CharField(max_length=500, choices=SOCIAL_ASSETS_CHOICES)
    legitimacy = models.CharField(max_length=50, choices=LEGITIMACY_CHOICES)
    microtarget = models.CharField(max_length=500, choices=MICROTARGET_CHOICES)
    channels = models.CharField(max_length=500, choices=CHANNEL_CHOICES)

# Execute model with its choices
PUMP_PRIMING_CHOICES = [
    ('Trail Content', 'Trial Content'),
    ('Bait Legitimate influencers', 'Bait Legitimate influencers'),
    ('Seek kernel of truth', 'Seek Kernel of truth'),
    ('Seed distortions', 'Seed distortions'),
    ('Use fake experts', 'Use fake experts'),
    ('Use Search','Use Search Engine Optimization'),
    ('Employ Commercial Analytic Firms','Employ Commercial Analytic Firms'),

]
CONTENT_DELIVERY_CHOICES = [
    ('Deliver ads', 'Deliver ads'),
    ('Social media', 'Social Media'),
    ('Traditional media','Traditional media'),
    ('Post Content','Post Content'),
    ('Share memes','Share memes'),
    ('Post Violative Content','Post Violative Content'),
    ('One-Way Direct Posting','One-Way Direct Posting'),
    ('Comment or Reply on Content','Comment or Reply on Content'),
    ('Post inauthentic social media comment','Post inauthentic social media comment'),
    ('Attract Traditional Media','Attract Traditional Media'),
]

EXPOSURE_MAXIMIZATION_CHOICES = [
    ('flooding the information space', 'flooding the information space'),
    ('Trolls amplify and manipulate', 'Trolls amplify and manipulate'),
    ('Hijack existing hashtag', 'Hijack existing hashtag'),
    ('Bots Amplify via Automated Forwarding','Bots Amplify via Automated Forwarding'),
    ('Utilize Spamoflauge','Utilize Spamoflauge'),
    ('Conduct Swarming','Conduct Swarming'),
    ('Conduct Keyword squatting','Conduct Keyword squatting'),
    ('inauthentic Sites Amplify News','inauthentic Sites Amplify News'),
    ('Amplify Existing Narratives','Amplify Existing Narratives'),
    ('Cross Posting','Cross Posting'),
    ('Post Across Groups','Post Across Groups'),
    ('Post Across Platform','Post Across Platform'),
    ('Post Across Discipline','Post Across Discipline'),
    ('Incentive Sharing','Incentive Sharing'),
    ('use Affiliate Marketing programs','use Affiliate Marketing programs'),
    ('Use Contests and prizes','Use Contests and prizes'),
    ('Manipulate platform Algorithm','Manipulate platform Algorithm'),
    ('Bypass Content Blocking','Bypass Content Blocking'),
    ('Direct Users to Alternative Platforms','Direct Users to Alternative Platforms'),

]

ONLINE_HARMS_CHOICES = [
    ('Censor social Media', 'Censor Social Media as a political Science'),
    ('Harass', 'Harass'),
    ('Boycott/"Cancel', 'Boycott/"Cancel" Opponents'),
    ('Harass People Based on Identities', 'Harass People Based on Identities'),
    ('Threaten to Dox','Threaten to Dox'),
    ('Dox','Dox'),
    ('Block Content','Block Content'),
    ('Destroy Information Generation','Destroy Information Generation'),
    ('Conduct Server Redirect','Conduct Server Redirect'),
    ('Suppress Opposition','Suppress Opposition'),
    ('Report Non-Violative','Report Non-Violative'),
    ('Goad People into Harmful','Goad People into Harmful Action'),
    ('Exploit Platform TOS/Content','Exploit Platform TOS/Content'),
    ('Platform Filtering','Platform Filtering'),
]

OFFLINE_ACTIVITY_CHOICES = [
    ('Conduct fundraising', 'Conduct fundraising'),
    ('Conduct Crowdfunding', 'Conduct Crowdfunding'),
    ('Organize Events', 'Organize Events'),
    ('Pay for Physical Action', 'Pay for Physical Action'),
    ('Conduct Symbolic Action', 'Conduct Symbolic Action'),
    ('Sell Merchandise', 'Sell Merchandise'),
    ('Encourage Attendance', 'Encourage Attendance'),
    ('Call to action to attend','Call to action to attend'),
    ('Facilitate logistics or support for attendance', 'Facilitate logistics or support for attendance'),
    ('Physical Violence', 'Physical Violence'),
    ('Conduct Physical Violence', 'Conduct Physical Violence'),
    ('Encourage Physical Violence', 'Encourage Physical Violence'),

]
PERSIST_INFORMATION_CHOICES = [
    ('Play the long game', 'Play the long game'),
    ('Continue to Amplify', 'Continue to Amplify'),
    ('Conceal People', 'Conceal People'),
    ('Use Pseudonyms', 'Use Pseudonyms'),
    ('Conceal Network Identity', 'Conceal Network Identity'),
    ('Distance Reputable Individuals', 'Distance Reputable Individuals'),
    ('Launder Accounts', 'Launder Accounts'),
    ('Change name of Accounts','Change name of Accounts'),
    ('Conceal Operational Activity', 'Conceal Operational Activity'),
    ('Conceal Network Identity', 'Conceal Network Identity'),
    ('Generate Content Unrelated', 'Generate Content Unrelated'),
    ('Break Association with Content', 'Break Association with Content'),
    ('Delete URLS', 'Delete URLS'),
    ('Coordinate on encrypted networks','Coordinate on encrypted networks'),
    ('Deny involvement','Deny involvement'),
    ('Delete Accounts','Delete Accounts'),
    ('Redirect URLS','Redirect URLS'),
    ('Remove Post Origins','Remove Post Origins'),
    ('Misattribute Activity','Misattribute Activity'),
    ('Conceal Infrustructure','Conceal infrustructure'),
    ('Utilize Bulletproof','Utilize Bulletproof'),
    ('Use Shell organizations','Use Shell Organizations'),
    ('Use Cryptocurrency','Use Cryptocurrency'),
    ('Obfuscate Payment','Obfuscate Payment'),
    ('Exploit TOS/Content','Exploit TOS/Content'),
    ('Legacy web content','Legacy web content'),
    ('Post Borderline Content','Post Borderline Content'),

]
class Execute(models.Model):
    pump_priming = models.CharField(max_length=500, choices=PUMP_PRIMING_CHOICES)
    content_delivery = models.CharField(max_length=500, choices=CONTENT_DELIVERY_CHOICES)
    exposure_maximization = models.CharField(max_length=500, choices=EXPOSURE_MAXIMIZATION_CHOICES)
    online_harms = models.CharField(max_length=500, choices=ONLINE_HARMS_CHOICES)
    offline_activity = models.CharField(max_length=500, choices=OFFLINE_ACTIVITY_CHOICES)
    persist_information = models.CharField(max_length=500, choices=PERSIST_INFORMATION_CHOICES)

class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('image', 'Image'),
    ]

    title = models.CharField(max_length=255, help_text="Title of the media")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES,
                                  help_text="Type of media: video, pdf, or image")
    description = models.TextField(blank=True, null=True,
                                   help_text="Description of the media (e.g., video description, PDF summary)")

    # Video-specific fields
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="URL of the video")
    video_source = models.CharField(max_length=255, blank=True, null=True,
                                    help_text="Source of the video (e.g., YouTube, Vimeo)")

    # PDF-specific fields
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    pdf_summary = models.TextField(blank=True, null=True, help_text="Summary or description of the PDF")
    pdf_url = models.URLField(blank=True, null=True, help_text="URL for accessing the PDF")

    # Image-specific field
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title