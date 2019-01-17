import axios from 'axios'

const service = axios.create({
  baseURL: 'http://10.4.20.85:8000', // api的base_url
  timeout: 3000000 // request timeout
})

// request interceptor
service.interceptors.request.use(config => {
  // Do something before request is sent
  return config
}, error => {
  // Do something with request error
  console.log(error) // for debug
  Promise.reject(error)
})

// respone interceptor
service.interceptors.response.use(
  response => response)

export default service
