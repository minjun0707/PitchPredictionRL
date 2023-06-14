package com.gachon.baseball;
import lombok.Data;

@Data
public class DetectionRequest {

    public String name;
    public String balls;
    public String strikes;
    public String on_3b;
    public String on_2b;
    public String on_1b;
    public String outs_when_up;
    public String inning;
    public String pitch_number;
    public String score_difference;
    public String pre1;
    public String pre2;
    public String pre3;
    public String stand;
    public String stand_L;
    public String stand_R;

    public void changeForJson() {
        changeStandForJson();
        changeBaseForJson();
    }

    private void changeStandForJson() {
        if(stand.equals("right")) {
            stand_R = "1";
            stand_L = "0";
        } else {
            stand_R = "0";
            stand_L = "1";
        }
    }

    private void changeBaseForJson() {
        if(on_1b.equals("true"))
            this.setOn_1b("1");
        else
            this.setOn_1b("0");

        if(on_2b.equals("true"))
            this.setOn_2b("1");
        else
            this.setOn_2b("0");

        if(on_3b.equals("true"))
            this.setOn_3b("1");
        else
            this.setOn_3b("0");
    }


    @Override
    public String toString() {
        return "FormResponse{" +
                "name='" + name + '\'' +
                "balls='" + balls + '\'' +
                ", strikes='" + strikes + '\'' +
                ", on_3b='" + on_3b + '\'' +
                ", on_2b='" + on_2b + '\'' +
                ", on_1b='" + on_1b + '\'' +
                ", outs_when_up='" + outs_when_up + '\'' +
                ", inning='" + inning + '\'' +
                ", pitch_number='" + pitch_number + '\'' +
                ", score_difference='" + score_difference + '\'' +
                ", pre1='" + pre1 + '\'' +
                ", pre2='" + pre2 + '\'' +
                ", pre3='" + pre3 + '\'' +
                ", stand='" + stand + '\'' +
                ", stand_L='" + stand_L + '\'' +
                ", stand_R='" + stand_R + '\'' +
                '}';
    }
}



