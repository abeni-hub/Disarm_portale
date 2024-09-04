from django.db import models

# Define choices as tuples for each attribute
STRATEGY_CHOICES = [
    ('offensive', 'Offensive'),
    ('defensive', 'Defensive'),
    ('neutral', 'Neutral'),
]

OBJECTIVE_CHOICES = [
    ('disrupt', 'Disrupt'),
    ('influence', 'Influence'),
    ('monitor', 'Monitor'),
]

TARGET_AUDIENCE_CHOICES = [
    ('public', 'General Public'),
    ('military', 'Military'),
    ('political', 'Political'),
]

# Define Plan model
class Plan(models.Model):
    strategy = models.CharField(max_length=50, choices=STRATEGY_CHOICES)
    objective = models.CharField(max_length=50, choices=OBJECTIVE_CHOICES)
    target_audience_analysis = models.CharField(max_length=50, choices=TARGET_AUDIENCE_CHOICES)

# Prepare model with its choices
NARRATIVE_CHOICES = [
    ('positive', 'Positive'),
    ('negative', 'Negative'),
    ('neutral', 'Neutral'),
]

CONTENT_CHOICES = [
    ('text', 'Text'),
    ('video', 'Video'),
    ('image', 'Image'),
]

LEGITIMACY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
]

MICROTARGET_CHOICES = [
    ('demographics', 'Demographics'),
    ('behavioral', 'Behavioral'),
    ('geographical', 'Geographical'),
]

CHANNEL_CHOICES = [
    ('social_media', 'Social Media'),
    ('news', 'News'),
    ('blogs', 'Blogs'),
]

AFFORDANCE_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
]

class Prepare(models.Model):
    narrative = models.CharField(max_length=50, choices=NARRATIVE_CHOICES)
    content = models.CharField(max_length=50, choices=CONTENT_CHOICES)
    legitimacy = models.CharField(max_length=50, choices=LEGITIMACY_CHOICES)
    microtarget = models.CharField(max_length=50, choices=MICROTARGET_CHOICES)
    channels = models.CharField(max_length=50, choices=CHANNEL_CHOICES)
    affordance = models.CharField(max_length=50, choices=AFFORDANCE_CHOICES)

# Execute model with its choices
PUMP_PRIMING_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

CONTENT_DELIVERY_CHOICES = [
    ('scheduled', 'Scheduled'),
    ('real_time', 'Real-Time'),
]

EXPOSURE_MAXIMIZATION_CHOICES = [
    ('viral', 'Viral'),
    ('organic', 'Organic'),
    ('paid', 'Paid'),
]

ONLINE_HARMS_CHOICES = [
    ('trolling', 'Trolling'),
    ('fake_news', 'Fake News'),
    ('phishing', 'Phishing'),
]

OFFLINE_ACTIVITY_CHOICES = [
    ('protests', 'Protests'),
    ('rallies', 'Rallies'),
    ('campaigns', 'Campaigns'),
]

class Execute(models.Model):
    pump_priming = models.CharField(max_length=50, choices=PUMP_PRIMING_CHOICES)
    content_delivery = models.CharField(max_length=50, choices=CONTENT_DELIVERY_CHOICES)
    exposure_maximization = models.CharField(max_length=50, choices=EXPOSURE_MAXIMIZATION_CHOICES)
    online_harms = models.CharField(max_length=50, choices=ONLINE_HARMS_CHOICES)
    offline_activity = models.CharField(max_length=50, choices=OFFLINE_ACTIVITY_CHOICES)
