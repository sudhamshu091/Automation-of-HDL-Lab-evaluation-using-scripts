module top(SW,LEDR);
  input [1:0] SW;
  output [0:0] LEDR;
  and_gate(SW[0],SW[1],LEDR);
endmodule
