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