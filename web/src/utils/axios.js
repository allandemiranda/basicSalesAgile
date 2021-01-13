import axios from 'axios';

const https = require('https');

const agent = new https.Agent({
  rejectUnauthorized: false,
});

const instance = axios.create({
  baseURL: 'https://localhost:5000/api/',
  responseType: 'json',
  httpsAgent: agent
});

export default instance;