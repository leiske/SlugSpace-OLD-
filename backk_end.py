import os
import time
import random
import json
import string
import random
import scipy
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
#from flask import Flask, request, session, g, redirect, url_for, abort, \render_template, flash
#setup website folders, static folder is available for css and javascript, templates folder is used to place jinja template
 @app.route('/')
 def index():
-    return render_template('index.html', title=title)
+    return render_template('index.html', title=title,carsInLot=2,remainingSpots=18,parkingLot="East Remote")

@app.route('/p/prototype')
def proto_ex:       
  main_data = {'north_remote':{'slots_available':100,'cars_in':2, 'cars_out':0}, 'west_remote':{'slots_available':100,'cars_in':2, 'cars_out':0}, 'east_remote':{'slots_available':100 ,'cars_in':2, 'cars_out':0}}

  def inventory_main(lot):
      st = main_data[lot]
      count = st['slots_available'] - st['cars_in'] + st['cars_out']
      if count <= 0:
          new_slots = 0
      elif count >= 100:
          new_slots = 100
      else:
          new_slots = count
      return {'slots_available':new_slots, 'cars_in':0}

  #def cars_in(dragon_brda, lot):
  #    if bool(dragon_brda) == True:

      #registr_b = bool(dragon_brdb)


  def simul_rn():
      m = 12
      if m > 0:
          s = True
      else:
          s = False
      switches = {'on':0,'off':0}
      while m>0:
          #print(bool(random.getrandbits(1)))
          time.sleep(0.1)
          m = m - random.getrandbits(1)
          #print(m)
          val = random.randint(0,2)
          if val< 2:
              switches['on'] = switches['on'] + 1
          else:
              switches['off'] = switches['off'] + 1
      return switches

  for n in range(4):
      print('Old dictionary data for north remote is: %s'%main_data['north_remote'])
      main_data['north_remote'] = inventory_main('north_remote')
      new_data = simul_rn()['on']
      new_out = simul_rn()['off']
      main_data['north_remote']['cars_in'] = new_data
      main_data['north_remote']['cars_out'] = new_out
      print('Dictionary data for north remote is: %s'%main_data['north_remote'])



 if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
    
 
