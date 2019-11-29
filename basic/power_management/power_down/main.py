import degu
import ujson
import time

if __name__ == '__main__':
    reported = {'state':{'reported':{}}}

    print("power down after 10 seconds...")
    time.sleep(10)

    reported['state']['reported']['state'] = 'power_down'

    print(ujson.dumps(reported))
    degu.update_shadow(ujson.dumps(reported))

    degu.power_down()
