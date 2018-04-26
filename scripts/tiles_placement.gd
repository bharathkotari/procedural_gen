extends Node2D

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var map1
var player
var cam1
var wm
var i=0
var j
var prev
var ra
var top_tile=0
var bottom_tile=1
var uphill=4
var downhill=6
var up_joint=5
var down_joint=7
func _ready():
	# Called every time the node is added to the scene.
	# Initialization here
	map1=get_node("TileMap")
	#map1.set_global_pos(Vector2(-30,10))
	player=get_node("Sprite")
	#player.set_global_pos(Vector2(300,0))
	player.set_pos(Vector2(50,300))
	wm=map1.world_to_map(Vector2(0,0))
	randomize()
	
	set_process(true)
	
func _process(delta):
	if (i<100):
		ra=round(rand_range(4,8))
		if(i==0):
			map1.set_cell(i,ra,top_tile)
			prev=ra
			fill_ground(i,ra)
		elif(i-1==0):
			map1.set_cell(i,prev,top_tile)
			fill_ground(i,prev)
		elif(ra<prev)and(i-1>1) and (map1.get_cell(i-2,prev)==top_tile)and (prev-1>=4):
			map1.set_cell(i,prev-1,top_tile)
			fill_ground(i,prev-1)
			prev=prev-1
		elif(ra<prev)and(i-1>1)and(map1.get_cell(i-2,prev+1)==top_tile)and(prev+1<=7):
			map1.set_cell(i,prev-1,uphill)
			map1.set_cell(i,prev,up_joint)
			fill_ground(i,prev)
			prev=prev-1
		
		
		elif(ra>prev)and(i-1>0) and (map1.get_cell(i-2,prev)==top_tile)and (prev+1<=7):
			map1.set_cell(i,prev+1,top_tile)
			prev=prev+1
			fill_ground(i,prev)
		elif(ra>prev)and(i-1>0)and(map1.get_cell(i-2,prev-1)==top_tile)and(prev-1>=4):
			map1.set_cell(i,prev,downhill)
			map1.set_cell(i,prev+1,down_joint)
			fill_ground(i,prev+1)
			prev=prev+1
		else:
			map1.set_cell(i,prev,top_tile)
			fill_ground(i,prev)
			
	i=i+1
	if(Input.is_action_pressed("ui_right")):
		#print(player.get_pos())
		player.set_global_pos(Vector2(player.get_pos().x+10,300))
		
	
	
func fill_ground(r,c):
	for m in range(c+1,10):
		map1.set_cell(r,m,bottom_tile)
