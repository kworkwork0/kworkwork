// Animchar render component
//
AnimcharRendComponent::AnimcharRendComponent():
  lodres(NULL),
  scene(NULL),
  sceneOwned(true),
  visBits(VISFLG_RENDERABLE),
  sceneBeforeRenderedCalled(false),
  magic(MAGIC_VALUE),
  noAnimDist2(0),
  noRenderDistSq(0),
  bsphRadExpand(0)
{
  ownerTm.row0 = V_C_UNIT_1000;
  ownerTm.row1 = V_C_UNIT_0100;
  ownerTm.row2 = V_C_UNIT_0010;
}

AnimcharRendComponent::~AnimcharRendComponent()
{
  if (sceneOwned)
    del_it(scene);
  lodres = NULL;
}
