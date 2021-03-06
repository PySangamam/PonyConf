from django.conf import settings

from jinja2.sandbox import SandboxedEnvironment

import pytz


def talk_to_dict(talk):
    return {
        'title': talk.title,
        'description': talk.description,
        'category': str(talk.category),
        'accepted': talk.accepted,
        'confirmed': talk.confirmed,
        'start_date': talk.start_date.astimezone(tz=pytz.timezone(settings.TIME_ZONE)) if talk.start_date else None,
        'duration': talk.estimated_duration,
        'track': str(talk.track) if talk.track else '',
        'video': talk.video,
        'speakers': list(map(speaker_to_dict, talk.speakers.all())),
    }


def speaker_to_dict(speaker, include_talks=False):
    d = {
        'name': speaker.name,
        'email': speaker.email,
    }
    if include_talks:
        d.update({
            'talks': list(map(talk_to_dict, speaker.talk_set.all())),
        })
    return d


def volunteer_to_dict(volunteer):
    return {
        'name': volunteer.name,
        'email': volunteer.email,
        'phone_number': volunteer.phone_number,
        'sms_prefered': volunteer.sms_prefered,
        'activities': list(map(lambda activity: activity.name, volunteer.activities.all())),
    }


class TalkEnvironment(SandboxedEnvironment):
    def __init__(self, talk, speaker, **options):
        super().__init__(**options)
        self.globals.update({
            'talk': talk_to_dict(talk),
            'speaker': speaker_to_dict(speaker),
        })


class SpeakerEnvironment(SandboxedEnvironment):
    def __init__(self, speaker, **options):
        super().__init__(**options)
        self.globals.update({
            'speaker': speaker_to_dict(speaker, include_talks=True),
        })


class VolunteerEnvironment(SandboxedEnvironment):
    def __init__(self, volunteer, **options):
        super().__init__(**options)
        self.globals.update({
            'volunteer': volunteer_to_dict(volunteer),
        })
