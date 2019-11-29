import degu
import ujson

if __name__ == '__main__':
    reported = {'state':{'reported':{}}}

    while True:
        reported['state']['reported']['state'] = 'suspend'

        print(ujson.dumps(reported))
        degu.update_shadow(ujson.dumps(reported))

        degu.suspend(30)
