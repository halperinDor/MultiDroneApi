from django.contrib.postgres.fields import ArrayField
from django.db import models


class MissionsCoordinates(models.Model):
    missions = ArrayField(
        ArrayField(
            ArrayField(
                models.FloatField(),
                size=2,
            ),
        ),
    )