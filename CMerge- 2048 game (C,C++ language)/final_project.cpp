#include <graphics.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROW 4
#define COL 4

//Function prototypes
char getInput();
void assign(int num[ROW][COL]);
void mathNum(int num[ROW][COL], char input);
void printStructure();
void moveNumbers(int num[ROW][COL], char input);
void goRight(int i,int end,int num[ROW][COL]);
void goLeft(int i,int end,int num[ROW][COL]);
void goUp(int i,int end,int num[ROW][COL]);
void goDown(int i,int end,int num[ROW][COL]);
int startPosX(int j);
int startPosY(int i);
void printArray(int num[ROW][COL]);
int gameOver(int num[ROW][COL]);
void scoreStore();
void checkHScore();

int score=0;
int highScore=0;

int main(){
    int gd=DETECT, gm;
    initgraph(&gd,&gm,"C:\\TC\\BGI");

	int num[ROW][COL]={{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};

	srand(time(0));

	checkHScore();

    assign(num);
	setbkcolor(WHITE);
	cleardevice();
	
    printArray(num);

    char input;
    input=getInput();
    while(input!='q'){
        moveNumbers(num,input);
        mathNum(num,input);
        printArray(num);
		printf("The score is: %d\n",score);
		if(gameOver(num)){
			break;
		}
		//break;
        input=getInput();		
    }

	scoreStore();
	checkHScore();

	//End game output
	cleardevice();
	setbkcolor(GREEN);
	setcolor(BLUE);
	int font = 3, direction = 0, font_size = 2;
	settextstyle(font,direction, font_size);
	outtextxy(300,200,"GAME OVER");

	printf("Game Over");

	getch();
    closegraph();

    return 0;
}

//Function to get user input 
char getInput() {
    char input;
    while (1) {
        printf("Enter direction: ");
		input=getch();


       
        if (input == 'w' || input == 'a' || input == 's' || input == 'd' || input == 'W' || input == 'A' || input == 'S' || input == 'D' || 
            input == 'q' || input =='Q') {
            return tolower(input);           
        }
        else {
            printf("Invalid input! Please enter w, a, s, d, or q to quit.\n");
        }
    }
}

//Function flor assigning position for 2s
void assign(int num[ROW][COL]) 
{
	int x;
    int y;
	int B = 1; //TRUE OF FALSE BOOL 
	
//ASSIGN
	do{
	//REROLL THE RANDOM POSITION ON EACH LOOP UNTIL A NEW PSOTION IS FILLED
		x = (rand() % 4 );	
		y = (rand() % 4 );
		for(int i = 0 ; i < COL; i++){
			for (int j = 0; j < ROW; j++){
				
				
			//THIS IS ASSIGNING FUCNTION
				if( (i == x) && (j == y)){ //GO TO RANDOM POSITION
					if (num[i][j] == 0){ //CHECK IF POSTION IS 0 OR NOT
						num[i][j] = 2;	//UPDATE IF SO 
						B = 0;	//BREAK WHILE LOOP
					}
					else{
						break; //BREAK FOR LOOP IF NOT 
					}
				}
			}
			
		}
	}while(B == 1); 

	//TESTING DISPLAY
	printf("\n");
	for(int i = 0; i < COL; i++){
		for( int j = 0; j < ROW; j++){
			printf("%d ", num[i][j]);
		}
		printf("\n");
	}
	//printf("X = %d, Y = %d\nCount = %d\n", x+1, y+1, count); //TESTING
}

//Function for calculating values
void mathNum(int num[4][4], char input){
	int move=0;

	for(int k =0; k < 4; k++){
		switch(input){//DIrection is expected to be 'w' 'a' 's' or 'd'
			//case for right
			case 'd':
				for(int i = 3; i > 0; i--){	
					if(num[k][i] == 0){
						for(int j  = 1; i-j >= 0 ; j++){
							if( num[k][i-j] != 0){
								num[k][i] = num[k][i-j];
								num[k][i-j] = 0;
								move=1;
								break;
							}					
						}
					} 
					if(num[k][i] != 0){
						for(int j  = 1; i-j >= 0 ; j++){
							if( (num[k][i-j] != 0) && (num[k][i-j] != num[k][i])){
								break;
							}
							else if(num[k][i-j] == num[k][i]){
								num[k][i] += num[k][i];
								score+=num[k][i];
								num[k][i-j] = 0;
								move=1;
								break;
							}					
						}
					}
				}	
				break;
			//case for left 
			case 'a':
				for(int i = 0; i < 3; i++){
					if(num[k][i] == 0){
						for(int j  = 1; i+j < 4 ; j++){
							if( num[k][i+j] != 0){
								num[k][i] = num[k][i+j];
								num[k][i+j] = 0;
								move=1;
								break;
							}					
						}
					} 
					if(num[k][i] != 0){
						for(int j  = 1; i+j < 4 ; j++){
							if( (num[k][i+j] != 0) && (num[k][i+j] != num[k][i])){
								break;
							}
							else if(num[k][i+j] == num[k][i]){
								num[k][i] += num[k][i];
								score+=num[k][i];
								num[k][i+j] = 0;
								move=1;
								break;
							}					
						}
					}
				}	
				break;
			//case for up 
			case 'w':		
				for(int i = 0; i < 3; i++){
					if(num[i][k] == 0){
						for(int j  = 1; i+j < 4 ; j++){
							if( num[i+j][k] != 0){
								num[i][k] = num[i+j][k];
								num[i+j][k] = 0;
								move=1;
								break;
							}					
						}
					} 
					if(num[i][k] != 0){
						for(int j  = 1; i+j < 4 ; j++){
							if( (num[i+j][k] != 0) && (num[i+j][k] != num[i][k])){
								break;
							}
							else if(num[i+j][k] == num[i][k]){
								num[i][k] += num[i][k];
								score+=num[i][k];
								num[i+j][k] = 0;
								move=1;
								break;
							}					
						}
					}
				}	
				break;
			//case for down
			case 's':
				for(int i = 3; i > 0; i--){
					if(num[i][k] == 0){
						for(int j  = 1; i-j >= 0 ; j++){
							if( num[i-j][k] != 0){
								num[i][k] = num[i-j][k];
								num[i-j][k] = 0;
								move=1;
								break;
							}					
						}
					} 
					if(num[i][k] != 0){
						for(int j  = 1; i-j >= 0 ; j++){
							if( (num[i-j][k] != 0) && (num[i-j][k] != num[i][k])){
								break;
							}
							else if(num[i-j][k] == num[i][k]){
								num[i][k] += num[i][k];
								score+=num[i][k];
								num[i-j][k] = 0;
								move=1;
								break;
							}					
						}
					}
				}	
				break;
			//case of e for exit game (only used to avoid oddity with default, can be removed)
			case 'e':
				break;
			default:
				printf("\nDEFUALT CASE FOUND\n");
				break;
		}
	}
	if(move==1){
		assign(num);
	}
	
}

//Function to print the entire grid, heading and everything
void printStructure(){
    //setbkcolor(WHITE);
    int font = 3, direction = 0, font_size = 5;
    settextstyle(font, direction, font_size);
    setcolor(YELLOW);
    outtextxy(215,30,"CMerge");

    setcolor(BLUE);
    rectangle(190,80,440,330);

    line(252,80,252,330);
    line(315,80,315,330);
    line(377,80,377,330);

    line(190,142,440,142);
    line(190,205,440,205);
    line(190,267,440,267);    
    
    settextstyle(font, direction, 2);

    setcolor(BLACK);
    outtextxy(50,350,"Rules:");
    settextstyle(font, direction, 1);
    outtextxy(80,370,"\"A\"--> Left,  \"W\"--> Up,");
    outtextxy(80,390,"\"S\"-->Down,  \"D\"--> Right");
    outtextxy(80,410,"\"Q\"--> Quit");

	settextstyle(font, direction, 3);
	setcolor(CYAN);
	outtextxy(45,100,"Score:");
	outtextxy(15,180,"High Score:");
	
	char sco[6];
	sprintf(sco,"%d",score);

	char hSco[6];
	sprintf(hSco,"%d",highScore);

	setcolor(BROWN);
	outtextxy(70,120,sco);
	outtextxy(70,200,hSco);
}

//Function to move numbers across the Grid
void moveNumbers(int num[ROW][COL], char input){
    int start,end;

    switch(input){
        case 'w':
			start=285;
            end=95;
            break;
        case 'a':
			start=396;
            end=210;
            break;
        case 's':
			start=95;
            end=285;
            break;
        case 'd':
			start=210;
            end=396;
            break;
    }
    
    int i=0;

    //For Moving Numbers
    while(i<abs(end-start)){ //increments the coordinate one by one to give it an animation look
        cleardevice();
        printStructure();
        int font = 3, direction = 0, font_size = 4;  
        settextstyle(font, direction, font_size);
        setcolor(RED);
        if(input=='d'){
            goRight(i,end,num);   
        }
        if(input=='a'){
            goLeft(i,end,num);   
        }
        if(input=='w'){
            goUp(i,end,num);   
        }
        if(input=='s'){
            goDown(i,end,num);   
        }
        i++;
    }
}

//Funtion to move numbers towards right side
void goRight(int i,int end,int num[ROW][COL]){
	int x,y;
	char c[4];
	for(int k=0;k<ROW;k++){
		for(int j=0;j<COL;j++){
			if(num[k][j]!=0){
				x=startPosX(j); //to get the x coordinate of that position in the grid
				y=startPosY(k); //to get the y coordinate of that position in the grid
				sprintf(c,"%d",num[k][j]);
				if(x+i<=end){
					outtextxy(x+i,y,c);
				}
				else{
					outtextxy(end,y,c);
				}
			}
		}
	}
}

//Funtion to move numbers towards left side
void goLeft(int i,int end,int num[ROW][COL]){
	int x,y;
	char c[4];
	for(int k=0;k<ROW;k++){
		for(int j=0;j<COL;j++){
			if(num[k][j]!=0){
				x=startPosX(j); //to get the x coordinate of that position in the grid
				y=startPosY(k); //to get the y coordinate of that position in the grid
				sprintf(c,"%d",num[k][j]);
				//printf("i is %d\n",x+i);
				//printf("y is %d\n",y);
				if(x-i>=end){
					outtextxy(x-i,y,c);
				}
				else{
					outtextxy(end,y,c);
				}
			}
		}
	}
	
}

//Funtion to move numbers up
void goUp(int i,int end,int num[ROW][COL]){
	int x,y;
	char c[4];
	for(int k=0;k<ROW;k++){
		for(int j=0;j<COL;j++){
			if(num[k][j]!=0){
				x=startPosX(j); //to get the x coordinate of that position in the grid
				y=startPosY(k); //to get the y coordinate of that position in the grid
				sprintf(c,"%d",num[k][j]);
				//printf("i is %d\n",x+i);
				//printf("y is %d\n",y);
				if(y-i>=end){
					outtextxy(x,y-i,c);
				}
				else{
					outtextxy(x,end,c);
				}
			}
		}
	}
}

//Funtion to move numbers down
void goDown(int i,int end,int num[ROW][COL]){
	int x,y;
	char c[4];
	for(int k=0;k<ROW;k++){
		for(int j=0;j<COL;j++){
			if(num[k][j]!=0){
				x=startPosX(j); //to get the x coordinate of that position in the grid
				y=startPosY(k); //to get the y coordinate of that position in the grid
				sprintf(c,"%d",num[k][j]);
				//printf("i is %d\n",x+i);
				//printf("y is %d\n",y);
				if(y+i<=end){
					outtextxy(x,y+i,c);
				}
				else{
					outtextxy(x,end,c);
				}
			}
		}
	}
}

//Function to get the y-coordinate for position on graphics window
int startPosX(int j){
	
	if(j==0){
		return 210;
	}
	else if(j==1){
		return 273;
	}
	else if(j==2){
		return 335;
	}
	else if(j==3){
		return 396;
	}
}

//Function to get the x-coordinate for position on graphics window
int startPosY(int i){
	if(i==0){
		return 95;
	}
	else if(i==1){
		return 160;
	}
	else if(i==2){
		return 220;
	}
	else if(i==3){
		return 285;
	}
}

//Function to print the array on graphics window
void printArray(int num[ROW][COL]){
	//setbkcolor(WHITE);
    printStructure();
	char c[4];
	int x,y;
	for(int i=0;i<ROW;i++){
		for(int j=0;j<COL;j++){
			if(num[i][j]!=0){
				x=startPosX(j);
				y=startPosY(i);

				sprintf(c,"%d",num[i][j]);
				//printf("%s\n",c);
				int font = 3, direction = 0, font_size = 4;
    			settextstyle(font, direction, font_size);
				setcolor(RED);
				outtextxy(x,y,c);
			}
		}
	}
	
}

//Function to check if there are no possible moves OR if he has won the game
int gameOver(int num[ROW][COL]){
	for(int i=0;i<ROW;i++){
		for(int j=0;j<COL;j++){
			if(num[i][j]==4096){
				return 1;
			}
		}
	}

	//To check if there is any possible move
	for(int i=0;i<ROW;i++){
        for(int j=0;j<COL-1;j++){
            if(num[i][j]==0 || num[i][j+1]==0 ||num[i][j]==num[i][j+1]){
                return 0;
            }
        }
    }
    for(int j=0;j<COL;j++){
        for(int i=0;i<ROW-1;i++){
            if(num[i][j] ==0 || num[i+1][j]==0 || num[i][j]==num[i+1][j]){
                return 0;
            }
        }
    }
    return 1;
}

//Function to store the score
void scoreStore(){
	FILE *fptr;
	fptr=fopen("score.txt","a");
	fprintf(fptr,"%d\n",score);
	fclose(fptr);
}

//Function to check the high score
void checkHScore(){
	FILE *fptr;
	fptr=fopen("score.txt","r");
	int temp;
	while(fscanf(fptr,"%d",&temp)!=EOF){
		if(temp>highScore){
			highScore=temp;
		}
	}

}

    //(0,0) outtextxy(210,95,"4"); 
    //(1,0) outtextxy(273,95,"8");
    //(2,0) outtextxy(335,95,"4");  
    //(3,0) outtextxy(396,95,"8"); 

    //(0,1) outtextxy(210,160,"8");
    //(1,1) outtextxy(273,160,"4");  
    //(2,1) outtextxy(335,160,"8");
    //(3,1) outtextxy(396,160,"4");  

    //(0,2) outtextxy(210,220,"4");
    //(1,2) outtextxy(273,220,"8");  
    //(2,2) outtextxy(335,220,"4");
    //(3,2) outtextxy(396,220,"8"); 

    //(0,3) outtextxy(210,285,"8");
    //(1,3) outtextxy(273,285,"4");  
    //(2,3) outtextxy(335,285,"8");
    //(3,3) outtextxy(396,285,"4");   
