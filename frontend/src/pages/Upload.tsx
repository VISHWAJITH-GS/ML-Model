import React, { useState } from 'react'
import api from '../services/api'

export default function Upload() {
  const [file, setFile] = useState<File | null>(null)
  const [message, setMessage] = useState('')

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) return setMessage('Please select a file')
    const fd = new FormData()
    fd.append('file', file)
    try {
      const res = await api.post('/upload', fd, { headers: { 'Content-Type': 'multipart/form-data' } })
      setMessage('Upload successful: ' + JSON.stringify(res.data.data))
    } catch (err: any) {
      setMessage('Upload failed: ' + (err?.response?.data?.detail || err.message))
    }
  }

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input type="file" onChange={(e) => setFile(e.target.files?.[0] ?? null)} />
        <button type="submit">Upload</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  )
}
