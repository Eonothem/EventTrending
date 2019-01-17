import request from '@/api/config'

export default function search(word) {
  return request({
    datatype: 'json',
    method: 'POST',
    url: '/result',
    data: {
      "eventKey": word
    }
  })
}
