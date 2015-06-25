
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

// Transparent hull
color("azure",0.5)
    %difference()
    {
        cylinder(h=110,r1=62, r2=43,$fn=100);
        translate([0,0,-0.001])
            cylinder(h=108,r1=61, r2=42,$fn=100);
    }

// Top and bottom boards
color("green")
{
    cylinder(h=1.6,r=50,$fn=100);
    translate([0,0,103])
        cylinder(h=1.6,r=35,$fn=100);
}

// Neopixel light panels
for(i=[0:22.5:350])
    rotate([0,0,i])
        translate([-55,0,0])
            rotate([0,-80,0])
                translate([0,-6.75,0])
                {
                     color("green")
                        cube([109,13.5,1.6]);
                     for(j=[9:10:99])
                         translate([j,6,1.6])
                            rotate([0,0,90])
                                led5050();
                }
