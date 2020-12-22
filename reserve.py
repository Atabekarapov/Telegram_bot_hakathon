 elif message.text == "Продажа":
        list_= []
        for line in lines:
      
            try:
                a = line.split(',')
                linee = a[2]
                list_.append(linee)

            except:
                a = ''
    

        minim = max(list_)
        bot.send_message(chat_id, minim)

        