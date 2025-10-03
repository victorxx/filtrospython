from flask import Flask


app=Flask(__name__)

@app.route('/')
def rodar():
    return '''<!DOCTYPE html>
<html lang="pt-br">
    <head>

    </head>
    <body>
        <script>
            let data=new Date();
            data.setTime(data.getTime()+(24*60*60*1000));
            let expires='expires='+data.toUTCString();
            document.cookie='meu=vi;'+expires+';path=/';
           
            let cookies=document.cookie.split(';');
            for(let i=0;i<cookies.length;i++){
                let cookie=cookies[i].trim();
                if(cookie.startsWith('meu=vi')){
                    alert('cookie existe');
                    break;
                }else{
                alert('o cookie está sendo criado');
                break;
                }
            }
           
        
        
        </script>
    </body>
</html>'''

app.run(debug=True)
