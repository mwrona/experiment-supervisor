import scipy.optimize as scopt
import scalarmapi
import json
import draw


def call_scalarm(experiment_id, x):
    scalarmapi.schedule_point(experiment_id, x)
    return scalarmapi.get_result(experiment_id, x)


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

    f = lambda x: call_scalarm(config['experiment_id'], x)
    res = scopt.anneal(func=f,
                       x0=config['start_point'],
                       full_output=True,
                       schedule=config['schedule'],
                       lower=config['lower_limit'],
                       upper=config['upper_limit'],
                       maxiter=config['maxiter'],
                       dwell=config['dwell'])
    print json.dumps({'result': res[1], 'values': to_csv(res[0])})

    draw.draw(f, config['lower_limit'], config['upper_limit'], "fun", res[0][0], res[0][1], res[1])
