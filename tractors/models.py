from django.db import models

IMPLEMENTS_CHOICES = (
  ('harrow', 'Harrow'),
  ('cultivator', 'Cultivator'),
  ('Rotavator', 'Rotavator'),
  ('plough', 'Plough'),
  ('paddy Thrasher', 'Paddy Thrasher'),
  ('dumping Trailer', 'Dumping Trailer'),
  ('4 wheel Trailer', '4 Wheel Trailer'),
)
# Create your models here.
class tractor(models.Model):
  tractor_id = models.PositiveIntegerField()
  model_name = models.CharField(max_length=50)
  owner_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_Implements = models.CharField(max_length=50, choices=IMPLEMENTS_CHOICES)
  used_by = models.FloatField()

  def __str__(self):
    return f'tractor: {self.model_name} {self.owner_name}'
