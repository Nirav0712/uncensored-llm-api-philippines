# Uncensored LLM API for developers in the Philippines

> OpenAI-compatible API for teams shipping from Metro Manila to Mindanao. Taglish prompts understood, system prompt respected, no lecture stapled to the front of every reply. Base: https://uncensored-llm.sbs/v1

**API:** https://uncensored-llm.sbs/v1
**Site:** https://uncensored-llm.sbs

Most models are tuned for a market that is not yours: they answer in clipped English, and the moment a prompt touches politics, health, money or security they hand back a warning instead of an answer. For a product built for Filipino users that is a defect. This page documents an OpenAI-compatible API that answers the question as it was asked.

## Why it matters for builders in the Philippines

BPO work and local products share one requirement: the bot has to sound like a person from here, not like a translated manual. Taglish is not a bug to be corrected, it is how people type. The second problem is harder to work around — models that refuse ordinary topics like tuition, loans, health or penetration testing because a policy written for another market says so. Here the scope stays with your team while streaming, tool calling and JSON mode keep working exactly as before.

## Example call

```bash
export UNLLM_KEY="sk-..."
curl https://uncensored-llm.sbs/v1/chat/completions \
  -H "Authorization: Bearer $UNLLM_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"uncensored-llm","messages":[{"role":"user","content":"Explain plainly how crypto market cap is computed."}],"stream":true}'
```

```python
# pip install openai
from openai import OpenAI
client = OpenAI(base_url="https://uncensored-llm.sbs/v1", api_key="sk-...")
r = client.chat.completions.create(
    model="uncensored-llm",
    messages=[{"role": "user", "content": "Explain plainly how crypto market cap is computed."}],
)
print(r.choices[0].message.content)
```

```javascript
import OpenAI from "openai";
const ai = new OpenAI({ baseURL: "https://uncensored-llm.sbs/v1", apiKey: process.env.UNLLM_KEY });
const r = await ai.chat.completions.create({ model: "uncensored-llm", messages: [{ role: "user", content: "Explain plainly how crypto market cap is computed." }] });
console.log(r.choices[0].message.content);
```

## Where it actually gets used

| Case | Why |
|---|---|
| BPO-grade support | A bot that closes tickets instead of quoting policy. |
| Local content | Copy, scripts and emails in the register people actually speak. |
| Authorised testing | Security work inside a signed scope from the client. |
| Adult fiction (18+) | Explicit scenes between adults, no cutaway. |

## Latency from your island

Latency is decided by your ISP, not your region. Measure it from your own machine:

```bash
curl -o /dev/null -s -w '%{time_total}s\n' https://uncensored-llm.sbs/v1/models
```

| City | Region |
|---|---|
| Metro Manila | NCR |
| Quezon City | NCR |
| Makati | NCR |
| Cebu City | Central Visayas |
| Davao City | Davao Region |
| Iloilo City | Western Visayas |
| Bacolod | Negros Island |
| Baguio | Cordillera |
| Cagayan de Oro | Northern Mindanao |
| Clark | Central Luzon |
| Batangas City | CALABARZON |
| Zamboanga City | Zamboanga Peninsula |

## Questions we actually get

### Is it really OpenAI-compatible?

Yes. /v1/chat/completions, /v1/models and SSE streaming follow the same event format, so the official SDK works after a base_url change.

### Is there a free trial?

Current terms live at https://uncensored-llm.sbs. Any pricing change is announced there, not in this repo.

### What is blocked?

Illegal content, including any material involving minors. Outside of that, the response is about the request.

### Does it work with Open WebUI or LibreChat?

Yes. Both take an OpenAI-compatible base URL — paste https://uncensored-llm.sbs/v1 and your key.

### How do I protect my key?

Keep it in an environment variable per environment, rotate it, and never ship it in a frontend bundle or public repo.

## This documentation in other languages

- [pt-BR] https://brown1023.github.io/llm-api-sem-censura-brasil/
- [es-419] https://brown1023.github.io/api-llm-sin-censura-latam/
- [id-ID] https://ryuuless.github.io/uncensored-llm-api-indonesia/
- [vi-VN] https://ryuuless.github.io/uncensored-llm-api-vietnam/
- [tr-TR] https://askcode24.github.io/sansursuz-llm-api-turkiye/
- [de-DE] https://askcode24.github.io/uncensored-llm-api-deutschland/
- [es-ES] https://palazuel0s2004.github.io/api-llm-sin-censura-espana/
- [it-IT] https://palazuel0s2004.github.io/llm-api-senza-censura-italia/
- [en-IN] https://nirav0712.github.io/uncensored-llm-api-india/
- [ar] https://mohamedabderrehman.github.io/uncensored-llm-api-arabia/
- [ar-EG] https://mohamedabderrehman.github.io/uncensored-llm-api-egypt/

---

uncensored-llm.sbs — OpenAI-compatible API. Illegal content, including any material involving minors, is blocked. Everything else is on the caller.