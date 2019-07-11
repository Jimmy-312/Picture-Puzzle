# Picture-Puzzle
**Move the bricks to make the right picture**
# **It has these documents:**
## These are vs relevant *(it means you needn't see these as something important)*
+ /.vs
+ /Picture Puzzle.sln
+ /Picture Puzz.pyproj
## These are real codes
+ /main.py
+ /brick.py
+ /brick_group.py
+ /puzzlepicture.py
## btw,it's a picture to exam.If you want , you can change it anytime.
+ /example.jpg
-------------------
# Now I will introduce every doucument specifically.
## puzzlepicture.py *(include the core algorithm)*
### load_image
+ it needs two parameter which are lines(a tuple like (rows,columns)) and files(the picture's source)
+ it uses the **pillow** module to cut image
+ create every *brick* and add them to a *brick_group*
+ create the void bricks as *turn*
+ it returns a *brick_group*, a tuple including every image's height and width, the whole image's height and width, *turn*, a dict to store the answer and a *record* to record the move history
### recreate_map
+ it needs three parameter which is a *brick_group*, *turn* and times( **to some degrees**, it can decide the difficulty of map)
+ it can make the right image into a puzzle
+ it returns *brick_group* and *turn*
### get_choice
+ to get the bricks around the void brick
### move
+ it's difficult to explain it here **(so just think it as what you think or you can ask me)**
### get_loc
+ transform the mouse's location to a brick position
### fake_cheat
+ it just recover by the recorded history. *(so dumb)*
+ you can use it by press **F**
## brick.py *(a basic class)*
+ **pos**:store the position of bricks
+ **img**:[image object,ID]
## brick_group.py *(a class to store a series of ***bricks***)*
+ **add**:add the new *brick* to *brick_group*
+ **get_id**:get a dict connecting the *pos* and *ID*
+ **get_pod**:get all bricks' position
+ **remove**:remove the *brick* from group
+ it can be iterable
+ *brick_group[position or index]* returns a brick
+ *brick_group[position or index]=value* value must be a image object
## main.py *(an UI using the pygame)*
+ **end_win**:judge whether solve the puzzle
--------------------------------------
# That's all, thank you for your reading!
## **PS:it's very*n tired to write a README :(**
