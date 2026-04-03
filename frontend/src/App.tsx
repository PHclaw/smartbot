import React, { useState } from 'react'

export default function App() {
  const [showDemo, setShowDemo] = useState(false)
  const [demoMessages, setDemoMessages] = useState<Array<{role: string; content: string}>>([])
  const [demoInput, setDemoInput] = useState('')
  const [demoLoading, setDemoLoading] = useState(false)

  const features = [
    { icon: '🚀', title: '5-Min Setup', desc: 'Drag-and-drop config. No engineers needed.' },
    { icon: '🧠', title: 'AI-Powered', desc: 'RAG knowledge base. Understands intent like a human.' },
    { icon: '💬', title: 'Multi-Channel', desc: 'Web / WhatsApp / WeChat / Xiaohongshu' },
    { icon: '🔓', title: '100% Free & Open', desc: 'MIT License. Deploy anywhere. No vendor lock-in.' },
    { icon: '🔄', title: 'Human Handoff', desc: 'Seamless transfer to human agents.' },
    { icon: '📊', title: 'Analytics', desc: 'Conversation analysis, intent tracking.' },
  ]

  const handleDemoChat = async () => {
    if (!demoInput.trim()) return
    setDemoLoading(true)
    setDemoMessages(prev => [...prev, { role: 'user', content: demoInput }])
    const input = demoInput
    setDemoInput('')
    
    await new Promise(r => setTimeout(r, 800))
    let reply = "Thanks for reaching out! How can I help you today?"
    
    if (input.toLowerCase().includes('price') || input.toLowerCase().includes('cost')) {
      reply = "SmartBot is 100% FREE and open source!\n\nNo subscription. No per-message fees.\nMIT License - deploy anywhere you want.\n\nCheck out our GitHub for details."
    } else if (input.toLowerCase().includes('feature')) {
      reply = "SmartBot features:\n\n✅ AI-powered replies (RAG)\n✅ Multi-channel support\n✅ Human handoff\n✅ Analytics dashboard\n✅ 5-min deployment\n✅ 100% Open Source\n\nEverything you need, completely free."
    } else if (/^(hi|hello|hey)/i.test(input)) {
      reply = "Hi there! 👋 I'm SmartBot.\n\nI can help you with:\n• Product questions\n• Feature overview\n• Setup guide\n\nWhat would you like to know?"
    }
    
    setDemoMessages(prev => [...prev, { role: 'assistant', content: reply }])
    setDemoLoading(false)
  }

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-white/80 backdrop-blur-md z-50 border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center">
              <span className="text-white font-bold text-xl">S</span>
            </div>
            <span className="text-xl font-bold text-gray-900">SmartBot</span>
            <span className="px-3 py-1 bg-green-100 text-green-700 text-sm font-medium rounded-full">Free & Open Source</span>
          </div>
          <nav className="hidden md:flex items-center gap-8">
            <a href="#features" className="text-gray-600 hover:text-indigo-600 transition">Features</a>
            <a href="#demo" className="text-gray-600 hover:text-indigo-600 transition">Demo</a>
            <a href="https://github.com/PHclaw/smartbot" className="text-gray-600 hover:text-indigo-600 transition">GitHub</a>
          </nav>
          <div className="flex items-center gap-3">
            <a href="https://github.com/PHclaw/smartbot" className="px-5 py-2 border-2 border-indigo-600 text-indigo-600 rounded-lg hover:bg-indigo-50 transition font-medium">
              Star on GitHub ⭐
            </a>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="pt-32 pb-20 px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50" />
        <div className="absolute top-20 left-10 w-72 h-72 bg-indigo-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float" />
        <div className="absolute bottom-20 right-10 w-72 h-72 bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float" style={{animationDelay: '1s'}} />
        
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-green-100 text-green-700 rounded-full text-sm font-medium mb-8">
            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
            100% Free & Open Source (MIT License)
          </div>
          
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">
            AI Customer Service<br/>
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600">
              Completely Free
            </span>
          </h1>
          
          <p className="text-xl text-gray-600 mb-10 max-w-2xl mx-auto">
            Deploy in 5 minutes. Powered by AI. No vendor lock-in.
            <br/>Perfect for startups, small teams, and developers.
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <a href="https://github.com/PHclaw/smartbot" className="w-full sm:w-auto px-8 py-4 bg-indigo-600 text-white rounded-xl text-lg font-semibold hover:bg-indigo-700 transition shadow-xl shadow-indigo-200">
              View on GitHub →
            </a>
            <button onClick={() => document.getElementById('demo')?.scrollIntoView({behavior: 'smooth'})} className="w-full sm:w-auto px-8 py-4 bg-white text-gray-700 border-2 border-gray-200 rounded-xl text-lg font-medium hover:border-indigo-300 transition">
              Try Demo
            </button>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="py-20 bg-gray-50">
        <div className="max-w-6xl mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Everything You Need
            </h2>
            <p className="text-xl text-gray-500">
              A complete AI customer service solution - 100% free
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, i) => (
              <div key={i} className="p-6 bg-white rounded-2xl border border-gray-100 hover:shadow-lg hover:border-indigo-100 transition group">
                <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-500">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Demo */}
      <section id="demo" className="py-20 bg-gradient-to-br from-indigo-50 to-purple-50">
        <div className="max-w-4xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Try It Now
            </h2>
            <p className="text-xl text-gray-500">
              Chat with our AI - see how SmartBot works
            </p>
          </div>
          
          <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
            <div className="px-6 py-4 bg-gray-900 text-white flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center">
                <span className="text-white font-bold">S</span>
              </div>
              <div>
                <div className="font-medium">SmartBot Demo</div>
                <div className="text-xs text-gray-400">Try asking about features or pricing</div>
              </div>
            </div>
            
            <div className="h-80 overflow-y-auto p-6 space-y-4 bg-gray-50">
              {showDemo && demoMessages.length === 0 && (
                <div className="text-center py-4">
                  <div className="w-12 h-12 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-3 text-xl">🤖</div>
                  <p className="text-gray-600 font-medium">Hi! Ask me anything about SmartBot</p>
                  <p className="text-gray-400 text-sm mt-1">Try: "What are the features?" or "Is it free?"</p>
                </div>
              )}
              
              {!showDemo && (
                <div className="text-center py-8">
                  <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-4 text-3xl">💬</div>
                  <h3 className="font-medium text-gray-700 mb-2">Try SmartBot</h3>
                  <p className="text-sm text-gray-400 mb-4">Experience AI-powered customer service</p>
                  <button onClick={() => setShowDemo(true)} className="px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition">Start Chat</button>
                </div>
              )}
              
              {demoMessages.map((msg, i) => (
                <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div className={`max-w-[75%] px-4 py-3 rounded-2xl ${
                    msg.role === 'user'
                      ? 'bg-indigo-600 text-white rounded-br-sm'
                      : 'bg-white text-gray-800 rounded-bl-sm shadow-sm'
                  }`}>
                    <p className="whitespace-pre-wrap">{msg.content}</p>
                  </div>
                </div>
              ))}
              
              {demoLoading && (
                <div className="flex justify-start">
                  <div className="bg-white px-4 py-3 rounded-2xl rounded-bl-sm shadow-sm">
                    <div className="flex gap-1">
                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0ms'}}></span>
                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '150ms'}}></span>
                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '300ms'}}></span>
                    </div>
                  </div>
                </div>
              )}
            </div>
            
            <div className="p-4 border-t bg-white">
              <div className="flex gap-3">
                <input
                  type="text"
                  value={demoInput}
                  onChange={(e) => setDemoInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleDemoChat()}
                  placeholder="Type a message..."
                  className="flex-1 px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
                <button
                  onClick={handleDemoChat}
                  disabled={demoLoading || !demoInput.trim()}
                  className="px-6 py-3 bg-indigo-600 text-white rounded-xl hover:bg-indigo-700 disabled:bg-gray-300 transition font-medium"
                >
                  Send
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-gradient-to-br from-indigo-600 to-purple-600">
        <div className="max-w-3xl mx-auto text-center px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Ready to Get Started?
          </h2>
          <p className="text-xl text-indigo-100 mb-10">
            Star us on GitHub, fork it, and deploy today. No signup required.
          </p>
          <a href="https://github.com/PHclaw/smartbot" className="inline-block px-10 py-4 bg-white text-indigo-600 rounded-xl text-lg font-semibold hover:bg-indigo-50 transition shadow-xl">
            GitHub Repository →
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-400 py-12">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <div className="w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg"></div>
            <span className="font-bold text-xl text-white">SmartBot</span>
          </div>
          <p className="text-sm mb-6">100% Free & Open Source · MIT License</p>
          <div className="flex justify-center gap-6 text-sm">
            <a href="https://github.com/PHclaw/smartbot" className="hover:text-white transition">GitHub</a>
            <a href="#" className="hover:text-white transition">Documentation</a>
            <a href="#" className="hover:text-white transition">License</a>
          </div>
          <div className="mt-8 text-sm">
            © 2025 SmartBot. MIT License.
          </div>
        </div>
      </footer>
    </div>
  )
}
