#!/usr/bin/env python
"""
This script will test the math modules in the turtlekin package
"""

import unittest
import sys
import homework2.turtlekin as turtlekin
from math import pi, sqrt




class Angtest(unittest.TestCase):

    """This is the test class for part one of the assignment"""

    def test_first(self):

       
        self.assertAlmostEqual(turtlekin.angx(1.0,1.0,1.0,0.0),0.0)
        self.assertAlmostEqual(turtlekin.angx(1.0,1.0,1.0,1.0),0.0)

        self.assertAlmostEqual(turtlekin.angy(1.0,1.0,1.0,0.0),0.0)
        self.assertAlmostEqual(turtlekin.angy(1.0,1.0,1.0,1.0),0.0)

        self.assertAlmostEqual(turtlekin.angxdot(1.0,1.0,1.0,0.0),pi)
        self.assertAlmostEqual(turtlekin.angxdot(1.0,1.0,1.0,1.0),pi)
      
        self.assertAlmostEqual(turtlekin.angydot(1.0,1.0,1.0,0.0),2.0*pi)
        self.assertAlmostEqual(turtlekin.angydot(1.0,1.0,1.0,1.0),2.0*pi)
       
        self.assertAlmostEqual(turtlekin.angx2dot(1.0,1.0,1.0,0.0),0.0)
        self.assertAlmostEqual(turtlekin.angx2dot(1.0,1.0,1.0,1.0),0.0)

        self.assertAlmostEqual(turtlekin.angy2dot(1.0,1.0,1.0,0.0),0.0)
        self.assertAlmostEqual(turtlekin.angy2dot(1.0,1.0,1.0,1.0),0.0)

        self.assertAlmostEqual(turtlekin.linmath(1.0,1.0,1.0,0.0),sqrt(5.0)*pi)
        self.assertAlmostEqual(turtlekin.linmath(1.0,1.0,1.0,1.0),sqrt(5.0)*pi)

        self.assertAlmostEqual(turtlekin.angmath(1.0,1.0,1.0,0.0),0.0)
        self.assertAlmostEqual(turtlekin.angmath(1.0,1.0,1.0,1.0),0.0)


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, "initialangle", Angtest)
