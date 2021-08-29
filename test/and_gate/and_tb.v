module and_tb;
reg A,B;
wire Y;
integer mcd;
and_gate dut(.A(A), .B(B), .Y(Y));
initial
begin
mcd = $fopen("results.txt");
end
initial
begin
#5 A =0; B=0;
#5 A =0; B=1;
#5 A =1; B=0;
#5 A =1; B=1;
end
always@(*)
begin
$fdisplay(mcd,"%g,%b,%b,%b",$time,A,B,Y);
end
endmodule
