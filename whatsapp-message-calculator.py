import json

#TR - Kişiye göre mesaj sayısını hesaplar.
#EN - Calculates message count by person.
def messageCountPerPerson(lines):
    messageCounts =  {}
    for i in lines:
      if (i in messageCounts.keys()):
          messageCounts[i]=messageCounts[i]+1
      else:
          messageCounts[i]=1
    return messageCounts

#TR - Flood mesajları saymadan mesaj sayısını hesaplar.
#EN - Counts the number of messages without counting flood messages.
def messageCountPerPersonNoFlood(lines):
    messageCounts = {}
    lastPerson = ""
    for i in lines:
      if (i in messageCounts.keys()):
        if(i==lastPerson):
            continue;
        else:
            messageCounts[i]=messageCounts[i]+1
            lastPerson = i
      else:
          messageCounts[i]=1
          lastPerson = i
    return messageCounts

#TR - Bu fonksiyon 2. ve 3. parametrenin arasında kalan String'i döndürür.
#EN - This function returns the String between the 2nd and 3rd parameters.
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

substringFromWhatsappText = []
f = open('CHANGE HERE.txt', 'r+', encoding='utf-8')
lines = [line.rstrip('\n') for line in f]
f.close()

for i in lines:
    substringFromWhatsappText.append(find_between(i," - ",": "))

countsPerPersonDictionary = messageCountPerPerson(filter(None, substringFromWhatsappText))
countsPerPersonDictionaryNoFlood = messageCountPerPersonNoFlood(filter(None, substringFromWhatsappText))

with open('results.txt', 'w', encoding='utf-8') as file:
    file.write("Message counts per person: \n")
    file.write(json.dumps(countsPerPersonDictionary, ensure_ascii=False, indent=4))
    file.write("\nMessage counts per person(no-flood): \n")
    file.write(json.dumps(countsPerPersonDictionaryNoFlood, ensure_ascii=False, indent=4))



