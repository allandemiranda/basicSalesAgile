import axios from 'axios';

const https = require('https');

const agent = new https.Agent({
  rejectUnauthorized: false,
});

const instance = axios.create({
  baseURL: 'https://flask-agile:5000/api/',
  responseType: 'json',
  httpsAgent: agent
});

export default instance;