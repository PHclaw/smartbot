import React, { useState } from 'react'

export default function App() {
  const [showLogin, setShowLogin] = useState(false)
  const [showDemo, setShowDemo] = useState(false)
  const [demoMessages, setDemoMessages] = useState<Array<{role: string; content: string}>>([])
  const [demoInput, setDemoInput] = useState('')
  const [demoLoading, setDemoLoading] = useState(false)

  const features = [
    {
      icon: '🚀',
      title: '5 分钟上线',
      desc: '无需工程团队，拖拽配置即可完成接入'
    },
    {
      icon: '🧠',
      title: 'AI 精准回复',
      desc: 'RAG 知识库检索，像人工一样准确理解问题'
    },
    {
      icon: '💬',
      icon2: '🌐',
      title: '全渠道覆盖',
      desc: '网站 / WhatsApp / 微信 / 小红书 一键接入'
    },
    {
      icon: '💰',
      title: '按需计费',
      desc: '不用不花钱，超出部分按量计费，透明无套路'
    },
    {
      icon: '🔄',
      title: '无缝转人工',
      desc: 'AI 无法解决时，一键转接人工客服'
    },
    {
      icon: '📊',
      title: '数据驱动',
      desc: '对话分析、意图统计、满意度追踪'
    },
  ]

  const plans = [
    {
      name: '免费',
      price: '¥0',
      period: '/月',
      messages: '100 条',
      desc: '适合个人体验',
      features: ['1 个 Bot', '100 条消息/月', '1 个知识库 (10MB)', '基础分析'],
      cta: '免费试用',
      highlighted: false,
    },
    {
      name: '入门',
      price: '¥99',
      period: '/月',
      messages: '3,000 条',
      desc: '适合小团队',
      features: ['3 个 Bot', '3,000 条消息/月', '5 个知识库 (100MB)', '多渠道接入', '邮件通知'],
      cta: '立即购买',
      highlighted: true,
    },
    {
      name: '专业',
      price: '¥299',
      period: '/月',
      messages: '10,000 条',
      desc: '适合成长型企业',
      features: ['10 个 Bot', '10,000 条消息/月', '知识库无限', 'API 接入', '优先支持'],
      cta: '立即购买',
      highlighted: false,
    },
    {
      name: '企业',
      price: '¥799',
      period: '/月',
      messages: '50,000 条',
      desc: '适合大型企业',
      features: ['Bot 无限', '50,000 条消息/月', '私有化部署', '专属客服', 'SLA 保障'],
      cta: '联系销售',
      highlighted: false,
    },
  ]

  const handleDemoChat = async () => {
    if (!demoInput.trim()) return
    setDemoLoading(true)
    setDemoMessages(prev => [...prev, { role: 'user', content: demoInput }])
    const input = demoInput
    setDemoInput('')
    
    // 模拟 AI 回复
    await new Promise(r => setTimeout(r, 1000))
    let reply = "感谢您的消息！我们的智能客服可以帮助您解答各类问题。请问有什么可以帮到您的？"
    
    if (input.includes('价格') || input.includes('多少钱')) {
      reply = "我们提供灵活的套餐方案：\n• 免费版：100 条/月\n• 入门版：¥99/月\n• 专业版：¥299/月\n• 企业版：¥799/月\n\n请问您想了解哪个版本的详情呢？"
    } else if (input.includes('功能')) {
      reply = "SmartBot 的核心功能包括：\n\n✅ AI 智能回复 - RAG 知识库检索\n✅ 多渠道接入 - 网站/微信/WhatsApp\n✅ 无缝转人工 - AI + 人工协作\n✅ 数据分析 - 对话/意图/满意度\n✅ 5 分钟上线 - 无需编码\n\n您最感兴趣的是哪个功能？"
    } else if (input.includes('你好') || input.includes('hi') || input.includes('hello')) {
      reply = "您好！👋 我是 SmartBot 智能客服。\n\n我可以帮您：\n• 解答产品问题\n• 介绍价格方案\n• 演示使用流程\n\n请问有什么可以帮助您的？"
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
          </div>
          <nav className="hidden md:flex items-center gap-8">
            <a href="#features" className="text-gray-600 hover:text-indigo-600 transition">功能</a>
            <a href="#pricing" className="text-gray-600 hover:text-indigo-600 transition">定价</a>
            <a href="#demo" className="text-gray-600 hover:text-indigo-600 transition">演示</a>
            <a href="#docs" className="text-gray-600 hover:text-indigo-600 transition">文档</a>
          </nav>
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowLogin(true)}
              className="px-4 py-2 text-gray-700 hover:text-indigo-600 transition"
            >
              登录
            </button>
            <button className="px-5 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition font-medium shadow-lg shadow-indigo-200">
              免费试用
            </button>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="pt-32 pb-20 px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50" />
        <div className="absolute top-20 left-10 w-72 h-72 bg-indigo-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float" />
        <div className="absolute bottom-20 right-10 w-72 h-72 bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-float" style={{animationDelay: '1s'}} />
        
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-100 text-indigo-700 rounded-full text-sm font-medium mb-8">
            <span className="w-2 h-2 bg-indigo-500 rounded-full animate-pulse" />
            已为 1,000+ 企业提供服务
          </div>
          
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">
            告别昂贵客服<br/>
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-purple-600">
              AI 帮你接单
            </span>
          </h1>
          
          <p className="text-xl text-gray-600 mb-10 max-w-2xl mx-auto">
            5 分钟配置上线，比人工更懂客户。按消息计费，不用不花钱。
            <br/>出海电商 / 中小企业 / 跨境团队的首选 AI 客服。
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <button className="w-full sm:w-auto px-8 py-4 bg-indigo-600 text-white rounded-xl text-lg font-semibold hover:bg-indigo-700 transition shadow-xl shadow-indigo-200 animate-pulse-glow">
              免费开始 →
            </button>
            <button
              onClick={() => document.getElementById('demo')?.scrollIntoView({behavior: 'smooth'})}
              className="w-full sm:w-auto px-8 py-4 bg-white text-gray-700 border-2 border-gray-200 rounded-xl text-lg font-medium hover:border-indigo-300 transition"
            >
              观看演示
            </button>
          </div>
          
          <p className="mt-6 text-gray-400 text-sm">
            无需信用卡 · 5 分钟配置 · 永久免费版可用
          </p>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-5xl mx-auto px-4">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {[
              {value: '1,000+', label: '企业客户'},
              {value: '10M+', label: '服务消息'},
              {value: '98%', label: '问题解决率'},
              {value: '5分钟', label: '平均上线时间'},
            ].map((stat, i) => (
              <div key={i} className="text-center">
                <div className="text-3xl md:text-4xl font-bold text-indigo-600 mb-2">{stat.value}</div>
                <div className="text-gray-500">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="py-20">
        <div className="max-w-6xl mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              为什么选择 SmartBot？
            </h2>
            <p className="text-xl text-gray-500">
              开箱即用，比人工更专业，比竞品更便宜
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

      {/* Live Demo */}
      <section id="demo" className="py-20 bg-gradient-to-br from-indigo-50 to-purple-50">
        <div className="max-w-4xl mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              立即体验 AI 客服
            </h2>
            <p className="text-xl text-gray-500">
              试试和我们的 AI 客服对话，感受智能问答的能力
            </p>
          </div>
          
          <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
            {/* Chat Header */}
            <div className="px-6 py-4 bg-gray-900 text-white flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center">
                <span className="text-white font-bold">S</span>
              </div>
              <div>
                <div className="font-medium">SmartBot 演示</div>
                <div className="text-xs text-gray-400">在线 · AI 客服</div>
              </div>
            </div>
            
            {/* Chat Messages */}
            <div className="h-80 overflow-y-auto p-6 space-y-4 bg-gray-50">
              {!showDemo && (
                <div className="text-center py-8">
                  <div className="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-4 text-3xl">
                    💬
                  </div>
                  <h3 className="font-medium text-gray-700 mb-2">开始对话</h3>
                  <p className="text-sm text-gray-400 mb-4">点击下方按钮体验 AI 客服</p>
                  <button
                    onClick={() => setShowDemo(true)}
                    className="px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition"
                  >
                    开始对话
                  </button>
                </div>
              )}
              
              {showDemo && demoMessages.length === 0 && (
                <div className="text-center py-4">
                  <div className="w-12 h-12 bg-indigo-100 rounded-full flex items-center justify-center mx-auto mb-3 text-xl">
                    🤖
                  </div>
                  <p className="text-gray-600 font-medium">您好！我是 SmartBot</p>
                  <p className="text-gray-400 text-sm mt-1">可以问我关于价格、功能、使用方法等问题</p>
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
            
            {/* Chat Input */}
            <div className="p-4 border-t bg-white">
              <div className="flex gap-3">
                <input
                  type="text"
                  value={demoInput}
                  onChange={(e) => setDemoInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleDemoChat()}
                  placeholder="输入消息..."
                  className="flex-1 px-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
                <button
                  onClick={handleDemoChat}
                  disabled={demoLoading || !demoInput.trim()}
                  className="px-6 py-3 bg-indigo-600 text-white rounded-xl hover:bg-indigo-700 disabled:bg-gray-300 transition font-medium"
                >
                  发送
                </button>
              </div>
              <p className="text-xs text-gray-400 mt-2 text-center">
                演示模式 · 试试问"价格"、"功能"、"你好"
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section id="pricing" className="py-20">
        <div className="max-w-6xl mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              简单透明的定价
            </h2>
            <p className="text-xl text-gray-500">
              按需计费，不用不花钱，超出部分按量计费
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {plans.map((plan, i) => (
              <div
                key={i}
                className={`p-6 rounded-2xl ${
                  plan.highlighted
                    ? 'bg-gradient-to-br from-indigo-600 to-purple-600 text-white shadow-2xl scale-105'
                    : 'bg-white border border-gray-200'
                }`}
              >
                <h3 className={`text-lg font-semibold mb-1 ${!plan.highlighted && 'text-gray-900'}`}>
                  {plan.name}
                </h3>
                <p className={`text-sm mb-4 ${plan.highlighted ? 'text-indigo-200' : 'text-gray-500'}`}>
                  {plan.desc}
                </p>
                <div className="mb-6">
                  <span className="text-4xl font-bold">{plan.price}</span>
                  <span className={plan.highlighted ? 'text-indigo-200' : 'text-gray-500'}>{plan.period}</span>
                </div>
                <div className={`text-sm font-medium mb-6 ${plan.highlighted ? 'text-indigo-200' : 'text-gray-600'}`}>
                  {plan.messages}
                </div>
                <ul className="space-y-3 mb-8">
                  {plan.features.map((feature, j) => (
                    <li key={j} className="flex items-center gap-2">
                      <span className={plan.highlighted ? 'text-indigo-200' : 'text-green-500'}>✓</span>
                      <span className={plan.highlighted ? 'text-white' : 'text-gray-600'}>{feature}</span>
                    </li>
                  ))}
                </ul>
                <button className={`w-full py-3 rounded-xl font-medium transition ${
                  plan.highlighted
                    ? 'bg-white text-indigo-600 hover:bg-indigo-50'
                    : 'bg-indigo-600 text-white hover:bg-indigo-700'
                }`}>
                  {plan.cta}
                </button>
              </div>
            ))}
          </div>
          
          <p className="text-center text-gray-400 mt-8">
            所有套餐均包含免费消息，超出部分 ¥0.05/条 · 无隐藏费用 · 随时可取消
          </p>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-gradient-to-br from-indigo-600 to-purple-600">
        <div className="max-w-3xl mx-auto text-center px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            准备好提升客户体验了吗？
          </h2>
          <p className="text-xl text-indigo-100 mb-10">
            加入 1,000+ 企业，今天就开始用 AI 客服
          </p>
          <button className="px-10 py-4 bg-white text-indigo-600 rounded-xl text-lg font-semibold hover:bg-indigo-50 transition shadow-xl">
            免费开始试用 →
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-400 py-16">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid md:grid-cols-4 gap-12 mb-12">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <div className="w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg"></div>
                <span className="font-bold text-xl text-white">SmartBot</span>
              </div>
              <p className="text-sm">
                面向出海团队和中企业的 AI 客服 SaaS
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">产品</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition">功能</a></li>
                <li><a href="#" className="hover:text-white transition">定价</a></li>
                <li><a href="#" className="hover:text-white transition">演示</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">资源</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition">文档</a></li>
                <li><a href="#" className="hover:text-white transition">API</a></li>
                <li><a href="#" className="hover:text-white transition">帮助中心</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">公司</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white transition">关于我们</a></li>
                <li><a href="#" className="hover:text-white transition">博客</a></li>
                <li><a href="#" className="hover:text-white transition">联系我们</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-800 pt-8 text-sm text-center">
            © 2025 SmartBot. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  )
}
