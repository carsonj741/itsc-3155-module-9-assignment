# TODO: Feature 1
def test_list_all_movies(test_app):
    test_app.post('/movies',data=dict(title="Avengers:Endgame", director="Russo Brothers", rating="4"))
    test_app.post('/movies', data=dict(title="Bee Movie",director="Jerry Seinfeld", rating="1"))
    test_app.post('/movies', data=dict(title="The Room", director="Tommy Wiseau", rating="5"))
    
    response = test_app.get('/movies')
    responseData = response.data

    assert b"<tr><td>Avengers:Endgame</td><td>Russo Brothers</td><td>4/5</td></tr>" in responseData
    assert b"<tr><td>Bee Movie</th><td>Jerry Seinfeld</td><td>1/5</td></tr>" in responseData
    assert b"<tr><td>The Room</th><td>Tommy Wiseau</td><td>5/5</td></tr>" in responseData