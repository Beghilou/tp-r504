for ((i = 1; i <= 500; i++)); do
    # Utiliser curl pour faire l'appel

    response=$(curl -s http://localhost:83) 
    echo "Appel $i - $response"
done

