
var config = {}
config['domoticz_ip'] = 'http://10.1.1.10:8081';
config['app_title'] = 'Dashticz';
config['domoticz_refresh'] = '5';
config['dashticz_refresh'] = '60';
config['language'] = 'pl_PL';
config['timeformat'] = 'YYYY-MM-DD HH:mm';
config['translate_windspeed'] = 0;

//config['hide_topbar'] = 1;

//config['auto_positioning'] = 1;
//config['use_favorites'] = 1;
config['static_weathericons'] = 0;

var screens = {}
screens['default'] = {
  background: 'bg4.jpg',
  columns: [
    1,2
  ]
}

var columns = {}
columns[1] = {
  width: 4,
  blocks: [
    21,29,27,26,33,34,25,35,32
  ]
}
columns[2] = {
  width: 8,
  blocks: [
    'graph_meteo_te',
    'graph_meteo_ba',
    'graph_gorapd_tehu'
  ]
}

var blocks = {}
blocks[21] = {
  width: 6,
  protected: true
}
blocks[25] = {
  width: 6,
  icon: 'fas fa-sun'
}
blocks[26] = {
  width: 6,
  protected: true
}
blocks[27] = {
  width: 6,
  protected: true,
  icon: 'fas fa-tint'
}
blocks[28] = {
  width: 6
}
blocks[29] = {
  width: 6,
  protected: true
}
blocks[32] = {
  width: 12
}
blocks[33] = {
  width: 6,
  icon: 'fas fa-power-off',
}
blocks[34] = {
  width: 6,
  icon: 'fas fa-power-off',
}
blocks[35] = {
  width: 6
}
blocks['graph_meteo_te'] = {
  devices: [10],
  graphTypes: ['te','hu'],
  datasetColors: ['#FF0000','#00FF00'], //,'#0000FF'],
  height: '250px',
  width: 6,
  buttonsSize: 0,
  custom: {
    "48h": {
      range: 'day',
      filter: '48 hours',
      data: {
        temp: 'd.te_10',
        humi: 'd.hu_10',
//        baro: 'd.ba_10'
      }
    }
  }
}
blocks['graph_meteo_ba'] = {
  devices: [10],
  graphTypes: ['ba'],
  datasetColors: ['#0000FF'],
  height: '250px',
  width: 6,
  buttonsSize: 0,
  custom: {
    "48h": {
      range: 'day',
      filter: '48 hours',
      data: {
        baro: 'd.ba_10'
      }
    }
  }
}
blocks['graph_gorapd_tehu'] = {
  devices: [12],
  graphTypes: ['te','hu'],
  datasetColors: ['#FF0000','#00FF00'],
  height: '250px',
  width: 12,
  buttonsSize: 0,
  custom: {
    "48h": {
      range: 'day',
      filter: '48 hours',
      data: {
        temp: 'd.te_12',
        humi: 'd.hu_12'
      }
    }
  }
}
blocks['graph_gorapd_hu'] = {
  devices: [12],
  graphTypes: ['ba'],
  datasetColors: ['#0000FF'],
  height: '200px',
  width: 6,
  buttonsSize: 0
}
