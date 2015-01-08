import scipy.optimize as scopt
import json
import draw
from scalarmapi import Scalarm


def call_scalarm(x):
    scalarm.schedule_point(x)
    return scalarm.get_result(x)


def to_csv(data):
    s = str(data[0])
    for l in data[1:]:
        s += ','
        s += str(l)
    return s


if __name__ == "__main__":
    config_file = open('config.json')
    config = json.load(config_file)
    config_file.close()
    scalarm = Scalarm(config['user'],
                      config['password'],
                      config['experiment_id'],
                      config["address"],
                      config["parameters_ids"])

    res = scopt.anneal(func=call_scalarm,
                       x0=config['start_point'],
                       full_output=True,
                       schedule=config['schedule'],
                       lower=config['lower_limit'],
                       upper=config['upper_limit'],
                       maxiter=config['maxiter'],
                       dwell=config['dwell'])
    print json.dumps({'result': res[1], 'values': to_csv(res[0])})

    draw.draw(call_scalarm, config['lower_limit'], config['upper_limit'], "fun", res[0][0], res[0][1], res[1])
