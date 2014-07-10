from .controllers import primary
from .controllers import demo_loops
import inputs, outputs
import rospy
from basic_head_api.msg import MakeFaceExpr

class ManualHead:
  """
  Transmits the current neck, face and eye position without actually
  controlling anything.
  """

  def step(self, dt):
    self.head_output.transmit()

  def __init__(self):
    self.head_output = outputs.get_instance("full_head")