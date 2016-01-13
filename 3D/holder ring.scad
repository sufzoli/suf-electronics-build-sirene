
module led5050()
{
    // 5050 SMD LED
    // Body
    color("white")
        difference()
        {
            translate([-2.5,-2.5,0.1])
                    cube([5,5,1.6]);
            translate([-2.7,-2.7,2])        
                rotate([0,0,45])        
                    cube([2,2,1],center=true);
        }

    // Yellow spot    
    translate([0,0,0.701])
        color("yellow")
            cylinder(h=1,r=2,$fn=100);

    // Pin
    color("gray")
        for(i=[-1.6,0,1.6])
            for(j=[-1,1])
            {
                translate([j * 2.2,i,0.1])
                    cube([1,1,0.2],center=true);
                translate([j * 2.6,i,0.4])
                    cube([0.2,1,0.8],center = true);
            }
}

b = 15;
h = 15;
w = 3;

/*
// loudspeaker plate
difference()
{
union()
{
    difference()
    {
        cylinder(h=50,d=160,$fn=100);
        translate([0,0,3])
            cylinder(h=47.001,d=154,$fn=100);
        // assembly holes
        for(i = [[50,50,-1],[-50,50,-1],[50,-50,-1],[-50,-50,-1]])
            translate(i)
                cylinder(h=7,d=3.5,$fn=32);
        // loudspeaker mounting holes
        for(i = [[41,41,-1],[-41,41,-1],[41,-41,-1],[-41,-41,-1]])
            translate(i)
                cylinder(h=7,d=4.5,$fn=32);
        // back plate cutout
        translate([61,-60,3])
            cube([20,120,50]);

        translate([0,0,-0.5])
            cylinder(h=4,d=92,$fn=100);
    }
    // back plate
    translate([58,-51,0])
        cube([3,5,50]);
    translate([59.5,-46,3])
        // Extruded triangle
        rotate(a=[90,-90,-90])
            linear_extrude(height = w, center = true, convexity = 10, twist = 0)
                polygon(points=[[0,0],[h,0],[0,b]], paths=[[0,1,2]]);
    translate([58,46,0])
        cube([3,5,50]);
    translate([58,-51,0])
        cube([3,102,8]);
    translate([59.5,46,3])
        // Extruded triangle
        rotate(a=[90,-90,90])
            linear_extrude(height = w, center = true, convexity = 10, twist = 0)
                polygon(points=[[0,0],[h,0],[0,b]], paths=[[0,1,2]]);

    // cylinder(h=3, d= 20, $fn=100);
    for(i=[0:4])
    {
        difference()
        {
            cylinder(h=3, d=84-i*16, $fn=100);
            translate([0,0,-0.5])
                cylinder(h=4, d=76-i*16, $fn=100);
        }
    }
    for(i=[0:7])
        rotate([0,0,i*45])
            translate([-2,6,0])
                cube([4,40,3]);
}
translate([56,-44,10])
    rotate(a=[0,90,0])
        cylinder(h=7,d=2.5,$fn=100);
translate([56,44,10])
    rotate(a=[0,90,0])
        cylinder(h=7,d=2.5,$fn=100);
}
*/

/*
// PSU plate
difference()
{
    union()
    {
        difference()
        {
            cylinder(h=50,d=160,$fn=100);
            translate([0,0,3])
                cylinder(h=47.001,d=154,$fn=100);
            // assembly holes
            for(i = [[50,50,-1],[-50,50,-1],[50,-50,-1],[-50,-50,-1]])
                translate(i)
                    cylinder(h=7,d=3.5,$fn=32);
            // bottom hole
            translate([0,0,-0.5])
                cylinder(h=4,d=130,$fn=100);
        }
        // back bottom support
        translate([46,-48,0])
            cube([15,96,3]);
        
        // back plate
        translate([58,-51,0])
            cube([3,5,50]);
        translate([58,46,0])
            cube([3,5,50]);
        
        // PSU holding cross
        rotate([0,0,5])
        {
            difference()
            {
                union()
                {
                    for(i=[0:1])
                        rotate([0,0,i*90])
                            translate([-7.5,-70,0])
                                cube([15,140,3]);
                    translate([-26,3,0])
                        cylinder(h=8,d=9,$fn=100);
                    translate([29,3,0])
                        cylinder(h=8,d=9,$fn=100);
                    
                    translate([0,40,0])
                        cylinder(h=8,d=9,$fn=100);
                    translate([0,-40,0])
                        cylinder(h=8,d=9,$fn=100);
                }
            translate([-26,3,-0.001])
                cylinder(h=8.002,d=3.5,$fn=20);
            translate([29,3,-0.001])
                cylinder(h=8.002,d=3.5,$fn=20);
            }
       }
    }
    // back plate cutout
    translate([61,-60,-0.001])
        cube([20,120,50.002]);
}
*/


/*
// PSU
rotate([0,0,5])
    difference()
    {
            translate([-50,-49,8])
                color("gray")
                    cube([100,98,37]);
        translate([-26,3,7.5])
            cylinder(h=40,d=3,$fn=20);
        translate([29,3,7.5])
            cylinder(h=40,d=3,$fn=20);
    }
*/

// bottom ring
/*
union()
{
    difference()
    {
        union()
        {
            cylinder(h=3,d=160,$fn=100);
            for(i = [[50,50,3],[-50,50,3],[50,-50,3],[-50,-50,3]])
                translate(i)
                    cylinder(h=10,d=13.5,$fn=32);
        }
        // assembly holes
        for(i = [[50,50,-1],[-50,50,-1],[50,-50,-1],[-50,-50,-1]])
            translate(i)
                cylinder(h=15,d=3.5,$fn=32);
        for(i = [[50,50,8],[-50,50,8],[50,-50,8],[-50,-50,8]])
            translate(i)
                cylinder(h=15,d=8,$fn=32);
        // bottom hole
        translate([0,0,-0.5])
            cylinder(h=4,d=128,$fn=100);
    }
}
*/


// translate([0,0,200])
//{
// Holder ring
difference()
{
    union()
    {
        cylinder(h=3,d=160,$fn=100);
        cylinder(h=119, d1=122.5, d2=86, $fn=100);
    }
    translate([0,0,-0.001])
        cylinder(h=119, d1=116.5, d2=80, $fn=100);
    translate([0,0,14])
        cylinder(h=119, d=130,$fn=100);
        
    for(i = [[50,50,-1],[-50,50,-1],[50,-50,-1],[-50,-50,-1]])
        translate(i)
            cylinder(h=7,d=3.5,$fn=100);
}


/*
// Transparent hull
color("azure",0.5)
    %difference()
    {
        cylinder(h=111,d1=114, d2=80,$fn=100);
        translate([0,0,-0.001])
            cylinder(h=96,d1=104, d2=70,$fn=100);
        cube([150,150,150]);
    }
    
// Top and bottom boards
color("green")
{
    cylinder(h=1.6,d=90,$fn=100);
    translate([0,0,92])
        cylinder(h=1.6,d=60,$fn=100);
}

// Neopixel light panels
 for(i=[0:22.5:350])
    rotate([0,0,i])
        translate([-46,0,0])
            rotate([0,-81,0])
                translate([0,-6,0])
                {
                     color("green")
                        cube([95,12,1.6]);
                     for(j=[9:8.5:90])
                         translate([j,6,1.6])
                            rotate([0,0,90])
                                led5050();
                }
}
*/