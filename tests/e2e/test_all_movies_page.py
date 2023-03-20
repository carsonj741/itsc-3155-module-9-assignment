# TODO: Feature 1

def test_list_all_movies(test_app):
    test_app.post('/movies',data=dict(title="The Shawshank Redemption", director="Frank Darabont", rating="4"))
    test_app.post('/movies', data=dict(title="The Godfather",director="Francis Ford Coppola", rating="1"))
    test_app.post('/movies', data=dict(title="The Room", director="Tommy Wiseau", rating="5"))
    
    response = test_app.get('/movies')

    assert b"<tr><td>The ShawshankRedemption</td><td>Frank Darabont</td><td>4/5</td></tr>" in response.data
    assert b"<tr><td>The Godfather</th><td>Francis Ford Coppola</td><td>1/5</td></tr>" in response.data
    assert b"<tr><td>The Room</th><td>Tommy Wiseau</td><td>5/5</td></tr>" in response.data
