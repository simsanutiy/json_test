import json

in_file = open('json.txt', 'r', encoding='utf-8')
out_file = open('out.txt', 'w')

parsed = json.loads(in_file.read())
in_file.close()

out_file.write('<form name=\"' + parsed['form']['name'] + '\" postmessage=\"'
               + parsed['form']['postmessage'] + '\">')

for item in parsed['form']['items']:

    if item['type'] == 'filler':
        out_file.write('\n' + item['attributes']['message'])
        continue

    if item['type'] == 'select':
        out_file.write('\n<select')
        for attr in item['attributes']:
            if item['attributes'][attr] is False:
                continue
            if attr == 'options':
                continue
            out_file.write(' ' + attr + '=\"' + str(item['attributes'][attr])
                           + '\"')
        out_file.write('>')
        for option in item['attributes'][options]:
            out_file.write('<option value=\"' + option['value'] + '\"')
            if option['disabled']:
                out_file.write(' disabled')
            out_file.write('>' + option['text'] + '</option>')
        out_file.write('</select>')
        continue

    if item['type'] == 'radio':
        for option in item['attributes']['items']:
            out_file.write('\n<input type=\"radio\" value=\"' + option['value']
                           + '\" name=\"' + item['attributes']['name'] + '\"')
            if option['checked']:
                out_file.write(' checked')
            out.file.write('>' + option['label'] + '</input>')
        continue
    
    out_file.write('\n<input type=\"' + item['type'] + '\"')
    for attr in item['attributes']:
        if item['attributes'][attr] is False:
            continue
        print(item['attributes'][attr])
        out_file.write(' ' + attr + '=\"' + str(item['attributes'][attr])
                       + '\"')
    out_file.write('></input>')

out_file.write('\n</form>')

out_file.close()
