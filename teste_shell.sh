echo "primeira"
echo "========"
curl 'http://127.0.0.1:8000/api/bio/contagem?base=attga'

echo "segunda"
echo "========"
curl 'http://127.0.0.1:8000/api/bio/rna?base=attga'

echo "terceira"
echo "========"
curl 'http://127.0.0.1:8000/api/bio/base_inversa?base=attga'



#echo "primeira"
#echo "======== server"
#curl 'https://deploy-flask-1.herokuapp.com/api/bio/contagem?base=attga'
#
#echo "segunda"
#echo "======== server"
#curl 'https://deploy-flask-1.herokuapp.com/api/bio/rna?base=attga'
#
#echo "terceira"
#echo "========server"
#curl 'https://deploy-flask-1.herokuapp.com/api/bio/base_inversa?base=attga'


