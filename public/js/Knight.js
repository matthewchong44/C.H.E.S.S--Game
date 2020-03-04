class Knight extends Piece{
    constructor(position, source, type) {
        super(position,source,type);
    }

    getValidMoves(currentPosition) {
        let currentPos = Number(currentPosition);
        if (selectedPiece != currentPosition) {
            oldSelectedPiece = selectedPiece;
            selectedPiece = currentPosition;
            clearValidMoves();
            this.clean();
        }

        //right -> right -> up = -8
        //right -> right -> down = +12
        //up -> up -> right = -19
        //up -> up -> left = -21
        //left -> left -> up = -12
        //left -> left -> down = +8
        //down -> down -> right = +21
        //down -> down -> left = +19

        let knightMoves = [-8, 12, -19, -21, -12, 8, 21, 19];

        for (let i = 0; i < knightMoves.length; i++) {
            let option = currentPos + knightMoves[i];
            if (option >= 10 && option <= 88) {
                if (option % 10 == 0 || option % 10 == 9) {
                    continue;
                }
                if(document.getElementById(option.toString()).src == ""){
                    this.getMoveArray().push(option);
                }else{
                    this.checkCapture(option);
                }
            }
        }

        moveOptions = this.getMoveArray();
        this.highlightMoves(this.getMoveArray());

    }
}