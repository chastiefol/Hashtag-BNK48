"""
How to use pygal
1. open cmd
2. pip install pygal
3. copy this code in cmd
4. find file svg in window
"""
import os
import uuid
from pygal import *
pie_chart = Pie()
pie_chart.title = 'ประชากรไทย ชาย-หญิง พ.ศ.2557 ( คิดเป็น  %)'
pie_chart.add('ชาย',48.62)
pie_chart.add('หญิง',51.38)
pie_chart.render_to_file('thailand2014.svg')