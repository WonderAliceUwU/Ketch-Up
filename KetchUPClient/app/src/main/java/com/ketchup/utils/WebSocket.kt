package com.ketchup.utils

import android.content.Context
import android.util.Log
import com.ketchup.app.KetchUp
import okhttp3.*

class ChatWebSocketListener : WebSocketListener() {


    override fun onOpen(webSocket: WebSocket, response: Response) {
        // Handles the websocket connection opening
    }

    override fun onMessage(webSocket: WebSocket, text: String) {
        // Handles the message received event
        println(text)

    }

    override fun onClosing(webSocket: WebSocket, code: Int, reason: String) {
        // Handles the websocket connection closing
    }

    fun updateContext(context: Context){
    }

}

class ChatWebSocket{
    companion object{
        private var webSocket: WebSocket? = null
        private lateinit var webSocketListener: ChatWebSocketListener

        fun createConnection(context: Context){
            if(webSocket == null){
                val client = OkHttpClient()
                val request = Request.Builder().url("ws://" + ServerAddress.readUrl(context) + "/ws-test").build()
                webSocketListener = ChatWebSocketListener()
                webSocket = client.newWebSocket(request, webSocketListener)
            }
        }

        fun closeConnection(){
            webSocket?.close(1000, "")
        }

        fun sendMessage(message: String): Boolean {
            Log.i(null, "Message sent $message")
            return webSocket?.send(message) ?: false
        }

    }
}
